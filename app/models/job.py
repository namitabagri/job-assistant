from pydantic import BaseModel

class JobDescription(BaseModel):
    company: str
    role: str
    description: str