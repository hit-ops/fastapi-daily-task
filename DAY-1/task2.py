from fastapi import FastAPI

app = FastAPI()

#home page

@app.get("/")
def home():
    return {
        "message": "Welcome to the fastapi !"
    }
@app.get("/about")
def about():
    return {
        "message": "This is the about page!"
    }
@app.get("/users")
def users():
    return {
        "users" : ["Hitaishi","Rintu","Rohit","Sourav"]
    }