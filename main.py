from fastapi import FastAPI
from routers import add_routes

app = FastAPI()

@app.get("/")
def get_root():
    return {"message" : "Server is running brother"}

add_routes(app)