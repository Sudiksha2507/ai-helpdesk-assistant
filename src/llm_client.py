"""
llm_client.py
The "AG" in RAG (Augmented Generation).

Two modes, chosen automatically:

1. REAL LLM MODE - if a GEMINI_API_KEY is set (see .env.example), the
   retrieved knowledge-base text is stuffed into a prompt and sent to
   Google's Gemini API (it has a genuinely free tier, no credit card
   needed, which is why it's used here instead of OpenAI). The model
   writes a natural-language answer grounded in that retrieved text.

2. OFFLINE FALLBACK MODE - if no API key is set, the app still fully
   works: it just returns the retrieved article directly, formatted as
   an answer, with no LLM call. Useful for demoing without any setup,
   and for understanding what "augmentation" is doing before an LLM
   is even involved.
"""

import os
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-1.5-flash:generateContent"
)

SYSTEM_INSTRUCTIONS = (
    "You are a helpful IT helpdesk assistant. Answer the user's question "
    "using ONLY the documentation provided below. Keep the answer short "
    "and step-by-step. If the documentation doesn't cover the question, "
    "say you don't have information on that."
)


def is_live_mode() -> bool:
    return bool(GEMINI_API_KEY)


def _build_prompt(question: str, retrieved_text: str) -> str:
    return (
        f"{SYSTEM_INSTRUCTIONS}\n\n"
        f"Documentation:\n{retrieved_text}\n\n"
        f"User question: {question}\n"
        f"Answer:"
    )


def _call_gemini(prompt: str) -> str:
    response = requests.post(
        f"{GEMINI_URL}?key={GEMINI_API_KEY}",
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()


def generate_answer(question: str, retrieved: list) -> str:
    """
    retrieved: list of (article_dict, score) tuples from Retriever.retrieve().
    Returns the assistant's final reply text.
    """
    if not retrieved:
        return ("I couldn't find anything in the knowledge base that matches "
                "your question. Try rephrasing, or raise a ticket for a human to look at.")

    retrieved_text = "\n\n".join(a["text"] for a, _ in retrieved)

    if is_live_mode():
        try:
            prompt = _build_prompt(question, retrieved_text)
            return _call_gemini(prompt)
        except Exception as e:
            return (f"(LLM call failed: {e})\n\n"
                    f"Falling back to the raw article instead:\n\n{retrieved_text}")

    # Offline fallback: no LLM call, just hand back the best-matching article.
    top_title = retrieved[0][0]["title"]
    return (f"[Offline mode \u2014 no GEMINI_API_KEY set, so this is the retrieved "
            f"article directly rather than an LLM-generated answer]\n\n"
            f"Most relevant help article: {top_title}\n\n{retrieved_text}")
