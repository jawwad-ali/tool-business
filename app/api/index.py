# api/index.py
from fastapi import FastAPI
from . import chat, health # Import your route modules

# This 'app' instance is what Vercel will run
app = FastAPI()

# Include the routers from your other files
app.include_router(chat.router)
app.include_router(health.router)

# You can also define a root endpoint for basic testing
@app.get("/api")
def read_root():
    return {"message": "FastAPI server is running"}