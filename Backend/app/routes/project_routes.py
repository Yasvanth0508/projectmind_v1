from fastapi import APIRouter

from app.models.project_model import (
    CreateProjectRequest,
    ProjectResponse
)

from app.services.project_service import (
    create_project,
    get_all_projects
)

router = APIRouter()


@router.post("/projects")
def create_new_project(request: CreateProjectRequest):

    created_project = create_project(
        project_id=request.id,
        project_name=request.name
    )

    return {
        "message": "Project created successfully",
        "project": created_project
    }


@router.get("/projects")
def fetch_projects():

    projects = get_all_projects()

    return {
        "projects": projects
    }