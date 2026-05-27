from app.config import settings
from google import genai

# Gemini client
client = genai.Client(
    api_key=settings.gemini_api_key
)


def generate_rag_response(
    question,
    retrieved_chunks,
    conversation_history
):

    try:

        # Empty retrieval handling
        if not retrieved_chunks:

            return (
                "I couldn't find relevant information "
                "in the uploaded documents."
            )

        # Build document context
        document_context = "\n\n".join(
            [chunk["content"] for chunk in retrieved_chunks]
        )

        # Build conversation memory
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

If answer is not available in documents,
say:
"I couldn't find the answer in the uploaded documents."

PREVIOUS CONVERSATION:
{memory_context}

DOCUMENT CONTEXT:
{document_context}

CURRENT QUESTION:
{question}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"LLM Error: {e}")

        return "Error generating response."