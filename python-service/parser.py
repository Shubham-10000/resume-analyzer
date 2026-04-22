<<<<<<< ours
<<<<<<< ours
import pdfplumber
import re


def extract_text_from_pdf_file(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return clean_text(text)


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)  # remove special chars
    text = re.sub(r'\s+', ' ', text)          # remove extra spaces
    return text.strip()
=======
=======
>>>>>>> theirs
from __future__ import annotations

from pathlib import Path

import pdfplumber


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """Extract plain text from all pages in a PDF file."""
    path = Path(pdf_path)
    if not path.exists() or path.suffix.lower() != ".pdf":
        raise ValueError("A valid PDF path is required.")

    pages: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")

    return "\n".join(pages).strip()
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
