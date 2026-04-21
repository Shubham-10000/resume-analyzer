from parser import extract_text_from_pdf_file, clean_text

SKILLS = ["python", "sql", "aws", "docker", "apis", "javascript", "java", "c++", "html", "css"]
    
def extract_skills(text):
    words = set(text.split())
    found_skills = [skill for skill in SKILLS if skill in words]
    return found_skills


def analyze(resume_text, job_description):
    job_clean = clean_text(job_description)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_clean)

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    score = int(len(matched) / len(job_skills) * 100) if job_skills else 0

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }