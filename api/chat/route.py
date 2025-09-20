# api/health.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/health") # Use the full path here
async def handle_health():
    return {"status": "ok"}