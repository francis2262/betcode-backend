from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/convert")
def convert(req: CodeRequest):
    # Mock Bet9ja slip (sample data for now)
    slip = {
        "source": "bet9ja",
        "code": req.code,
        "legs": [
            {
                "home": "Arsenal",
                "away": "Chelsea",
                "market": "1X2",
                "pick": "HOME",
                "odds": 1.85
            },
            {
                "home": "Man Utd",
                "away": "Liverpool",
                "market": "GG",
                "pick": "YES",
                "odds": 1.70
            }
        ]
    }

    # Map to SportyBet equivalents (for demo)
    mapped = []
    for leg in slip["legs"]:
        if leg["market"] == "1X2":
            sporty_market = "Match Result"
        elif leg["market"] == "GG":
            sporty_market = "Both Teams To Score"
        else:
            sporty_market = "Unknown"
        mapped.append({**leg, "sporty_market": sporty_market})

    return {"original": slip, "mapped": mapped}
