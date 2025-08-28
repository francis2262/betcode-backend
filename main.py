from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI(title="Betcode Converter", description="Convert booking codes between betting platforms", version="1.0")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Your backend is live! 🎉"}
