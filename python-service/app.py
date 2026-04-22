from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from analyze import analyze_resume


class AnalyzeRequest(BaseModel):
    resume_text: str = Field(..., min_length=1)
    job_description: str = Field(..., min_length=1)


class AnalyzeResponse(BaseModel):
    score: float
    matched_skills: list[str]
    missing_skills: list[str]


app = FastAPI(title="Resume Analyzer API", version="1.0.0")


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    try:
        result = analyze_resume(
            resume_text=request.resume_text,
            job_description=request.job_description,
        )
    except Exception as exc:  # defensive API guard
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return AnalyzeResponse(
        score=result.score,
        matched_skills=result.matched_skills,
        missing_skills=result.missing_skills,
    )
