from fastapi import APIRouter
from schemas.restaurant_schema import Fooditem


restaurant_router = APIRouter(tags=["Restaurant Management System"],prefix="/res")

@restaurant_router.get("/{userid}/order")
def order_food(food_name:str,quantity:int):
    return {"message":f"Your {food_name} will be on your table in short period"}

@restaurant_router.get("/menu")
def show_menu():
    return {"message":"These are the food items"}

@restaurant_router.post("/{userid}/book-table")
def book_table(people_count:int):
    return {"message":f"Table booked for {people_count} successfully"}

@restaurant_router.post("/{userid}/bill")
def show_bill(food:Fooditem,count:int):
    total = food.price*count
    print(f"Your bill for {food.food_name} is {total}")
    return {"message":f"Your bill for {food.food_name} is {food.price*count}"}

@restaurant_router.post("/{userid}/payment")
def pay_bill(totalprice:float):
    return{"message": f"Sent {totalprice} to Restaurant"}


