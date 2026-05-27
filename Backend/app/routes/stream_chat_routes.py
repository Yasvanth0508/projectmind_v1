from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat_model import ChatRequest

from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_similar_chunks
from app.services.memory_service import (
    get_recent_chat_history
)
from app.services.message_service import store_message

from app.services.streaming_llm_service import (
    stream_rag_response
)

router = APIRouter()


@router.post("/stream-chat")
def stream_chat(request: ChatRequest):

    # Store the user message immediately
    try:
        store_message(
            chat_id=request.chat_id,
            role="user",
            content=request.question
        )
    except Exception as e:
        print("Failed to store user message:", e)

    # Generate embedding
    question_embedding = generate_embedding(
        request.question
    )

    # Retrieve chunks
    retrieved_chunks = retrieve_similar_chunks(
        query_embedding=question_embedding,
        project_id=request.project_id
    )

    # Conversation memory
    conversation_history = get_recent_chat_history(
        chat_id=request.chat_id
    )

    def generator_wrapper():
        assistant_text = ""

        for chunk in stream_rag_response(
            question=request.question,
            retrieved_chunks=retrieved_chunks,
            conversation_history=conversation_history
        ):
            assistant_text += chunk
            yield chunk

        if assistant_text.strip():
            try:
                store_message(
                    chat_id=request.chat_id,
                    role="assistant",
                    content=assistant_text
                )
            except Exception as e:
                print("Failed to store assistant message:", e)

    return StreamingResponse(
        generator_wrapper(),
        media_type="text/plain"
    )