from fastapi import APIRouter

from app.models.chat_session_model import (
    CreateChatRequest,
    UpdateChatTitleRequest
)

from app.services.chat_session_service import (
    create_chat,
    get_project_chats,
    update_chat_title
)

router = APIRouter()


@router.post("/chats")
def create_new_chat(request: CreateChatRequest):

    created_chat = create_chat(
        project_id=request.project_id,
        title=request.title
    )

    return {
        "message": "Chat created successfully",
        "chat": created_chat
    }


@router.patch("/chats")
def rename_chat(request: UpdateChatTitleRequest):

    updated_chat = update_chat_title(
        chat_id=request.chat_id,
        title=request.title
    )

    return {
        "message": "Chat title updated successfully",
        "chat": updated_chat
    }


@router.get("/chats/{project_id}")
def fetch_project_chats(project_id: str):

    chats = get_project_chats(project_id)

    return {
        "chats": chats
    }