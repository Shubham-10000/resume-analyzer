POST /analyze

Request:
{
"resume_text": "string",
"job_description": "string"
}

Response:
{
"score": number,
"matched_skills": [string],
"missing_skills": [string]
}
