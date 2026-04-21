from parser import extract_text_from_pdf_file
from analyze import analyze


if __name__ == "__main__":
    resume_path = "/Users/bunny/Documents/Colabration_projects/Resume_analyzer/python-service/Shubham_Sawant_Resume.pdf"

    resume_text = extract_text_from_pdf_file(resume_path)

    job_description = """
    Looking for a Python developer with experience in Amazon Web Services,
    Docker, REST APIs, and Machine Learning
    """

    result = analyze(resume_text, job_description)

    print(result)