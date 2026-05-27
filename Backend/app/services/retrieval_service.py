from app.db.supabase_client import supabase


def retrieve_similar_chunks(query_embedding, project_id, match_count=5):

    response = supabase.rpc(
        "match_documents",
        {
            "query_embedding": query_embedding,
            "match_count": match_count,
            "filter_project_id": project_id
        }
    ).execute()

    return response.data