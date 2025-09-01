from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

# Create FastAPI app
app = FastAPI()

# Route to serve your index.html
@app.get("/")
def read_root():
    # Automatically locate index.html in the same folder as main.py
    return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))

# Optional: Health check (Render uses this sometimes)
@app.get("/health")
def health_check():
    return {"status": "ok"}
