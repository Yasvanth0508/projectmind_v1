from app.db.supabase_client import supabase


def get_recent_chat_history(chat_id, limit=6):

    response = supabase.table("messages") \
        .select("*") \
        .eq("chat_id", chat_id) \
        .order("created_at", desc=True) \
        .limit(limit) \
        .execute()

    messages = response.data

    # Reverse to maintain conversation order
    messages.reverse()

    return messages