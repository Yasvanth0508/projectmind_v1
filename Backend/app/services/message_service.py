from app.db.supabase_client import supabase


def store_message(chat_id, role, content):

    response = supabase.table("messages").insert({
        "chat_id": chat_id,
        "role": role,
        "content": content
    }).execute()

    return response.data


def get_chat_messages(chat_id):

    response = supabase.table("messages") \
        .select("*") \
        .eq("chat_id", chat_id) \
        .order("created_at") \
        .execute()

    return response.data