from pydantic import BaseModel

class ApplicationSpecification(BaseModel):
    relevant_skills: list[str]
    relevant_experience: list[str]
    relevant_projects: list[str]
    skill_gaps: list[str]
    resume_focus: list[str]
    cover_letter_focus: list[str]