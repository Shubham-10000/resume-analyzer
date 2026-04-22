from fastapi import FastAPI
from pydantic import BaseModel
from analyze import analyze

app = FastAPI()


class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str
    
class AnalyzeResponse(BaseModel):
    score: int
    matched_skills: list[str]
    missing_skills: list[str]
    
    
@app.get('/')
def home():
    return {"message": "Welcome to the Resume Analyzer API!"}

@app.post('/analyze',response_model=AnalyzeResponse)
def analyze_resume(request:AnalyzeRequest):
    result = analyze(request.resume_text,request.job_description)
    return result