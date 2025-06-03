import os

def require_user_key():
    key = os.getenv("GOD_MASTER_KEY", "")
    return key.strip() == "lucipier"