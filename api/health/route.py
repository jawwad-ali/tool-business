# api/chat.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/api/chat") # Use the full path here
async def handle_chat():
    # Your chat logic here
    return {"message": "This is the chat endpoint"}