from pydantic import BaseModel

class Fooditem(BaseModel):
    food_name : str
    price : float

class Bill(BaseModel):
    food_name:str
    count:int
    price:float