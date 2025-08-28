from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Betcode Backend!"}

@app.get("/test")
def test():
    return {"status": "OK", "info": "Your backend is live!"}
