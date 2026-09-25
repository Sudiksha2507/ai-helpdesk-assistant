"""
app.py
Streamlit front-end for the AI IT Helpdesk Assistant.

Flow: user types a question -> retrieval.py finds the most relevant
knowledge-base article(s) -> llm_client.py generates a grounded answer
(real LLM if a key is set, offline fallback otherwise) -> if the user
is still stuck, they can raise a ticket, stored in MySQL via db.py.
"""

import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))

import db
from retrieval import Retriever, load_knowledge_base
from llm_client import generate_answer, is_live_mode

KB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base")


@st.cache_resource
def get_retriever():
    articles = load_knowledge_base(KB_PATH)
    return Retriever(articles)


st.set_page_config(page_title="AI IT Helpdesk Assistant", page_icon="\U0001F4BB")
st.title("\U0001F4BB AI IT Helpdesk Assistant")
st.caption(
    "LLM mode: " + ("\U0001F7E2 live (GEMINI_API_KEY set)" if is_live_mode()
                     else "\u26AA offline fallback (no GEMINI_API_KEY set)")
)

retriever = get_retriever()

# Keep the last answer in session state so the "raise a ticket" button
# below can see it without re-running retrieval.
if "last_question" not in st.session_state:
    st.session_state.last_question = ""
    st.session_state.last_answer = ""
    st.session_state.last_matches = []

st.subheader("Ask a question")
question = st.text_input("What's the issue?", placeholder="e.g. my wifi keeps disconnecting")

if st.button("Get help") and question.strip():
    with st.spinner("Searching the knowledge base..."):
        matches = retriever.retrieve(question, top_k=2)
        answer = generate_answer(question, matches)

    st.session_state.last_question = question
    st.session_state.last_answer = answer
    st.session_state.last_matches = matches

if st.session_state.last_answer:
    st.subheader("Answer")
    st.write(st.session_state.last_answer)

    if st.session_state.last_matches:
        with st.expander("Matched knowledge-base article(s)"):
            for article, score in st.session_state.last_matches:
                st.markdown(f"**{article['title']}**  (relevance: {score:.2f})")
    else:
        st.warning("Nothing in the knowledge base matched this well.")

    st.divider()
    st.subheader("Still stuck?")
    with st.form("ticket_form"):
        user_name = st.text_input("Your name")
        subject = st.text_input("Ticket subject", value=st.session_state.last_question)
        submitted = st.form_submit_button("Raise a support ticket")
        if submitted:
            if not user_name.strip():
                st.error("Please enter your name.")
            else:
                ticket_id = db.create_ticket(
                    user_name, subject, st.session_state.last_question,
                    st.session_state.last_answer,
                )
                st.success(f"Ticket #{ticket_id} created. A human will follow up.")

st.divider()
st.subheader("\U0001F4CB All tickets")
tickets = db.get_all_tickets()
if tickets:
    st.dataframe(
        [{"ID": t["id"], "From": t["user_name"], "Subject": t["subject"],
          "Status": t["status"], "Created": t["created_at"]} for t in tickets],
        use_container_width=True,
    )
else:
    st.caption("No tickets yet.")
