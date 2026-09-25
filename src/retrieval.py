"""
retrieval.py
The "R" in RAG (Retrieval-Augmented Generation).

Same idea as the TF-IDF matching in the Resume Screening project: turn the
user's question and every knowledge-base article into TF-IDF vectors, then
use cosine similarity to find which article is the closest match.
"""

import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _clean(text: str) -> str:
    text = text.lower()
    # Join hyphenated compounds (e.g. "Wi-Fi" -> "wifi") before stripping
    # other punctuation, so they match how people actually type queries.
    text = text.replace("-", "")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_knowledge_base(folder_path: str) -> list:
    """Returns a list of {"filename", "title", "text"} dicts, one per article."""
    articles = []
    for filename in sorted(os.listdir(folder_path)):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(folder_path, filename)
        with open(path) as f:
            text = f.read()
        first_line = text.strip().splitlines()[0]
        title = first_line.replace("Title:", "").strip()
        articles.append({"filename": filename, "title": title, "text": text})
    return articles


class Retriever:
    """
    Fits one TF-IDF vectorizer over the whole knowledge base up front, so
    each question only needs to be vectorized against that same vocabulary
    (fast, and keeps the "vector space" consistent).
    """

    def __init__(self, articles: list):
        self.articles = articles
        self.vectorizer = TfidfVectorizer(stop_words="english")
        corpus = [_clean(a["text"]) for a in articles]
        self.doc_vectors = self.vectorizer.fit_transform(corpus)

    def retrieve(self, question: str, top_k: int = 1, min_score: float = 0.05):
        """
        Returns up to top_k (article, score) tuples, best first, filtering
        out anything below min_score (i.e. "not actually related").
        """
        query_vector = self.vectorizer.transform([_clean(question)])
        scores = cosine_similarity(query_vector, self.doc_vectors)[0]

        ranked = sorted(
            zip(self.articles, scores), key=lambda pair: pair[1], reverse=True
        )
        return [(article, score) for article, score in ranked[:top_k] if score >= min_score]
