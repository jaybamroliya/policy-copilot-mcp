from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

POLICIES = {
    "read": ["status", "hello"],
    "execute": ["deploy", "run"]
}

@app.get("/")
def health():
    return {"status": "Policy Copilot running"}

@app.post("/authorize")
def authorize(req: TaskRequest):
    task = req.task.lower()

    for scope, actions in POLICIES.items():
        if task in actions:
            return {
                "allowed": True,
                "scope": scope,
                "message": f"Task '{task}' allowed under {scope}"
            }

    return {
        "allowed": False,
        "message": f"Task '{task}' NOT authorized"
    }
