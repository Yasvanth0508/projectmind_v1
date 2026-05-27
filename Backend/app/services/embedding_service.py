from app.config import settings
from google import genai

# Create Gemini client
client = genai.Client(
    api_key=settings.gemini_api_key
)


def generate_embedding(text):

    try:

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values

    except Exception as e:

        print(f"Embedding Error: {e}")

        return None