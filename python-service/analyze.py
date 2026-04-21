import re
from parser import clean_text


SKILLS = {
    "python", "sql", "aws", "docker", "api",
    "pandas", "numpy", "flask", "fastapi",
    "java", "spring", "linux",
    "machine learning", "data analysis", "data engineering"
}

SYNONYMS = {
    "amazon web services": "aws",
    "rest api": "api",
    "restful api": "api",
    "ml": "machine learning",
    "data analytics": "data analysis"
}

NORMALIZATION_MAP = {
    "apis": "api",
    "rest": "api",
    "restful": "api",
    "sqls": "sql",
    "py": "python"
}

STOPWORDS = {
    "and", "or", "with", "for", "in", "a", "the", "to", "of"
}


def apply_synonyms(text):
    text = text.lower()
    for phrase, standard in SYNONYMS.items():
        text = text.replace(phrase, standard)
    return text


def normalize_word(word):
    return NORMALIZATION_MAP.get(word, word)


def extract_skills(text):
    # Apply synonyms first, then clean
    text = apply_synonyms(text)
    text = clean_text(text)

    words = set(text.split())
    words = {normalize_word(w) for w in words if w not in STOPWORDS}

    found = set()

    # Word-based matching
    for skill in SKILLS:
        if " " not in skill and skill in words:
            found.add(skill)

    # Phrase-based matching using regex
    for skill in SKILLS:
        if " " in skill:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text):
                found.add(skill)

    return list(found)


def analyze(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = set(resume_skills) & set(job_skills)
    missing = set(job_skills) - set(resume_skills)

    score = int(len(matched) / len(job_skills) * 100) if job_skills else 0

    return {
        "score": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }