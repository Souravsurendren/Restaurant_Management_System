from fastapi import FastAPI
from routes.restaurant_routes import restaurant_router
from routes.user_routes import user_router


def add_routes(app:FastAPI):
    app.include_router(restaurant_router)
    app.include_router(user_router)