from pydantic import BaseModel

class CandidateProfile(BaseModel):
    name: str
    summary: str
    skills: list[str]
    experience: list[str]
    projects: list[str]
    education: list[str]