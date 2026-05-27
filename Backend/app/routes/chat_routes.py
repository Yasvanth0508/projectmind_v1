from fastapi import APIRouter

from app.models.chat_model import ChatRequest

from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_similar_chunks
from app.services.llm_service import generate_rag_response
from app.services.message_service import store_message
from app.services.memory_service import (
    get_recent_chat_history
)

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    # Store user message
    store_message(
        chat_id=request.chat_id,
        role="user",
        content=request.question
    )

    # Generate embedding
    question_embedding = generate_embedding(
        request.question
    )

    # Retrieve relevant chunks
    retrieved_chunks = retrieve_similar_chunks(
        query_embedding=question_embedding,
        project_id=request.project_id
    )

    # Get recent conversation history
    conversation_history = get_recent_chat_history(
        chat_id=request.chat_id
    )

    # Generate AI response
    answer = generate_rag_response(
        question=request.question,
        retrieved_chunks=retrieved_chunks,
        conversation_history=conversation_history
    )

    # Store assistant response
    store_message(
        chat_id=request.chat_id,
        role="assistant",
        content=answer
    )

    return {
        "question": request.question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks
    }