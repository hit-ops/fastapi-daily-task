from fastapi import FastAPI

app = FastAPI()

@app.post("/create_user")
def create_user(user: dict):
    return {
        "message": "User created successfully",
        "data": user
    }