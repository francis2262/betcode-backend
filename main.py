from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary in-memory database
class BetCode(BaseModel):
    code: str

@app.get("/")
def home():
    return {"message": "Bet Code Converter API is running!"}

@app.post("/convert")
def convert_code(data: BetCode):
    # Fake conversion (you can add real logic later)
    return {
        "original_code": data.code,
        "converted_code": "BET9JA-" + data.code[::-1]  # reverses the code just for now
    }
