from __future__ import annotations

import re
import string
from dataclasses import dataclass

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "was",
    "were",
    "will",
    "with",
    "you",
    "your",
}


@dataclass
class AnalysisResult:
    score: float
    matched_skills: list[str]
    missing_skills: list[str]


def normalize(text: str) -> str:
    """Lowercase and remove punctuation."""
    lowered = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    return lowered.translate(translator)


def tokenize(text: str) -> list[str]:
    """Split normalized text into words and keep alphabetic tokens."""
    return re.findall(r"[a-z][a-z0-9+#.\-]*", text)


def extract_keywords(text: str) -> set[str]:
    """Get simple keywords by removing stopwords and very short tokens."""
    cleaned = normalize(text)
    tokens = tokenize(cleaned)
    return {token for token in tokens if token not in STOPWORDS and len(token) > 2}


def analyze_resume(resume_text: str, job_description: str) -> AnalysisResult:
    """Compare resume against job description keywords and compute match score."""
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    matched = sorted(job_keywords.intersection(resume_keywords))
    missing = sorted(job_keywords.difference(resume_keywords))

    if not job_keywords:
        score = 0.0
    else:
        score = round((len(matched) / len(job_keywords)) * 100, 2)

    return AnalysisResult(
        score=score,
        matched_skills=matched,
        missing_skills=missing,
    )

