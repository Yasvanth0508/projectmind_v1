from pydantic import BaseModel


class CreateProjectRequest(BaseModel):
    id: str
    name: str


class ProjectResponse(BaseModel):
    id: str
    name: str