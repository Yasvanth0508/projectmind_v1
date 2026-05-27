from fastapi import APIRouter

from app.services.message_service import (
    get_chat_messages
)

router = APIRouter()


@router.get("/messages/{chat_id}")
def fetch_chat_messages(chat_id: str):

    messages = get_chat_messages(chat_id)

    return {
        "messages": messages
    }