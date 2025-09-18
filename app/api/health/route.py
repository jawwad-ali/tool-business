import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

load_dotenv(".env.local")

# Create a separate FastAPI app for this endpoint
app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "I am very Healthy!"}

# Vercel handler
handler = app