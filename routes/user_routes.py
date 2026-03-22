from fastapi import FastAPI,APIRouter
from schemas.user_schema import UserLogin,UserCreation

user_router = APIRouter(tags=["User"],prefix="/user")

@user_router.get("/")
def check_user():
    return {"message":"WORKING"}

@user_router.post("/login")
def user_login(user:UserLogin):
    return {"message":"User authenticated successfully"}

@user_router.post("/register")
def user_register(user:UserCreation):
    return {"message":"Your account has been created successfully"}