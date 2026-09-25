# AI IT Helpdesk Assistant

A Streamlit app that answers IT support questions using retrieval-augmented
generation (RAG) over a small troubleshooting knowledge base, with a MySQL
-backed ticket system for anything it can't resolve.

Matches the resume line: **Python, LLM, RAG, Streamlit, MySQL**.

## What it does

- **Ask a question** in plain English (e.g. "my wifi keeps disconnecting").
- **Retrieval**: the question is matched against 8 knowledge-base articles
  using TF-IDF + cosine similarity (same technique as the Resume Screening
  project) to find the most relevant one(s).
- **Generation**: the matched article's content is used to answer the
  question — either handed to a real LLM (if you set a free Gemini API key)
  to phrase a natural answer, or, with no key, returned directly as a
  clearly-labeled "offline mode" answer. **The app fully works either way**
  — the LLM is optional polish on top of working retrieval, not a
  requirement to demo it.
- **Ticket system**: if the answer doesn't help, the user can raise a
  ticket (stored in MySQL), viewable in a live table at the bottom of the page.

## Project structure

```
schema.sql                        -- 1 table: tickets
data/knowledge_base/*.txt         -- 8 troubleshooting articles (the "knowledge base")
src/
  app.py                          -- Streamlit UI (the whole user-facing app)
  retrieval.py                    -- the "R" in RAG: TF-IDF + cosine similarity search
  llm_client.py                   -- the "AG" in RAG: builds the prompt, calls Gemini or falls back
  db.py                           -- all MySQL access for the ticket system
requirements.txt
.env.example                      -- where to get a free API key, if you want one
```

## RAG in this project, explained simply (for an interview)

RAG = **R**etrieval-**A**ugmented **G**eneration: find relevant information
first, then have the model answer *using that information* instead of
guessing from what it was trained on. Three concrete steps, matching the
three files above:

1. **Retrieve** (`retrieval.py`): turn every knowledge-base article, and
   the user's question, into TF-IDF vectors sharing one vocabulary, then
   use cosine similarity to find the closest-matching article(s). A
   `min_score` cutoff means unrelated questions (e.g. "best pizza
   toppings") correctly return "nothing found" instead of a bad guess —
   worth demoing, since it shows the retrieval step actually filters.

2. **Augment**: the matched article's text gets inserted into the prompt
   sent to the LLM, alongside the user's question (see `_build_prompt` in
   `llm_client.py`). This is the "augmented" part — the model's context now
   includes your specific documentation, not just its training data.

3. **Generate** (`llm_client.py`): the LLM writes a natural-language answer
   grounded in that documentation. If no API key is set, this step is
   skipped and the raw matched article is shown instead — still useful,
   just not LLM-phrased.

**If asked "why Gemini and not OpenAI/ChatGPT":** Gemini has a genuinely
free tier with no credit card required, which matters for a student
project you might want to actually keep running. Swapping in another
LLM later only means changing `llm_client.py` — nothing else in the app.

## Setup

1. **MySQL**:
   ```
   mysql -u root < schema.sql
   mysql -u root -e "CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'apppass123';
                      GRANT ALL PRIVILEGES ON ai_helpdesk_assistant.* TO 'appuser'@'localhost';
                      FLUSH PRIVILEGES;"
   ```
   (Reuse the same `appuser` from the other two projects if you already made one.)

2. **Python packages**:
   ```
   pip install -r requirements.txt
   ```

3. *(Optional)* **Real LLM answers**: get a free key at
   https://aistudio.google.com/apikey and set it as the `GEMINI_API_KEY`
   environment variable (see `.env.example` for the exact commands per OS).
   Skip this entirely to run in offline fallback mode.

4. **Check `src/db.py`** — update `DB_CONFIG` if your MySQL user/password differ.

## Run

```bash
cd src
streamlit run app.py
```

This opens the app in your browser (usually `http://localhost:8501`). Try
asking about wifi, a forgotten password, a slow computer, a printer, or a
VPN issue — those all have matching articles in `data/knowledge_base/`.

## Extending it (good "next steps" to mention in an interview)

- Let admins add/edit knowledge-base articles from within the app instead of editing text files.
- Auto-close tickets once a similar question gets answered successfully.
- Swap the fixed knowledge base for a vector database (e.g. FAISS) if the
  article count grows past a few hundred — TF-IDF stays fast at this scale
  but doesn't handle semantic meaning as well as embeddings would.
