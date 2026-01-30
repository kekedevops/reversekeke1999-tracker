from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserData(BaseModel):
    email: str
    sign_on: str
    username: str
    uid: str
    current_level: int
    current_team: str
    team_summary: str
    objectives: str
    invite_code: str
    pulls: int
    daily_checklist: list[str]
    weekly_checklist: list[str]
    device: str

db = []

@app.post("/add_user/")
def add_user(data: UserData):
    db.append(data.dict())
    return {"message": "User added", "total_users": len(db)}

@app.get("/users/")
def get_users():
    return db