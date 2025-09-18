import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from openai import OpenAI

load_dotenv(".env.local")

# Create a separate FastAPI app for this endpoint
app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.post("/")
async def chat_endpoint(request: dict):
    """Simple chat endpoint that echoes back the message"""
    message = request.get("message", "")
    return {
        "response": f"You said: {message}",
        "timestamp": "2025-09-19T10:30:00Z",
        "status": "success"
    }

# Vercel handler
handler = app