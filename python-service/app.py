from parser import extract_text_from_pdf_file
from analyze import analyze

if __name__ == "__main__":
    text = extract_text_from_pdf_file(r"/Users/bunny/Documents/Colabration_projects/Resume_analyzer/python-service/Shubham_Sawant_Resume.pdf")
    
    #print("----- EXTRACTED TEXT -----")
    #print(text[:1000])
    
    job_description = """
    Looking for a Python developer with experience in SQL, AWS, Docker, and APIs
    """

    result = analyze(text, job_description)

    print(result)