import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from mangum import Mangum
from openai import OpenAI

load_dotenv(".env.local")

app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.get("/api/health")
async def health_check():
    return {"status": "I am very Healthy!"}

@app.post("/api/chat")
async def chat_endpoint(request: dict):
    """Simple chat endpoint that echoes back the message"""
    message = request.get("message", "")
    return {
        "response": f"You said: {message}",
        "timestamp": "2025-09-19T10:30:00Z",
        "status": "success"
    }

@app.get("/api")
def read_root():
    return {"message": "FastAPI server is running"}

# Vercel handler
handler = Mangum(app)