from app.config import settings
from google import genai

# Gemini client
client = genai.Client(
    api_key=settings.gemini_api_key
)


def stream_rag_response(
    question,
    retrieved_chunks,
    conversation_history
):

    # Empty retrieval handling
    if not retrieved_chunks:

        yield (
            "I couldn't find relevant information "
            "in the uploaded documents."
        )

        return

    # Build document context
    document_context = "\n\n".join([
        chunk["content"]
        for chunk in retrieved_chunks
    ])

    # Build memory context
    memory_context = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in conversation_history
    ])

    # Final prompt
    prompt = f"""
You are a helpful AI assistant.

Use BOTH:
1. Previous conversation
2. Uploaded document context

to answer naturally and accurately.

PREVIOUS CONVERSATION:
{memory_context}

DOCUMENT CONTEXT:
{document_context}

CURRENT QUESTION:
{question}
"""

    # Streaming response
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    for chunk in response:

        if chunk.text:
            yield chunk.text