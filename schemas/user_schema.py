from pydantic import BaseModel,Field,field_validator
import re #regex pattern

class UserLogin(BaseModel):
    username:str=Field(...,min_length=8)
    password:str=Field(...,min_length=8)

    @field_validator("username")
    def username_validation(cls,v):
        if not any(c.isupper() for c in v): #check every letters whether any of them is capital letter
            raise ValueError("Username must contain a capital letter!")
        return v
    
    @field_validator("password")
    def password_validation(cls,v):
        if not re.match(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).+$', v):
            raise ValueError("Password must contain capital, number, and special char")
        return v
    
class UserCreation(BaseModel):
    name:str
    username:str
    password:str=Field(...,min_length=8)
    phone_number:str

    @field_validator("password")
    def password_validation(cls,v):
        if not re.match(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).+$', v):
            raise ValueError("Password must contain capital, number, and special char")
        return v
    
    @field_validator("phone_number")
    def phone_number_validation(cls,v):
        if len(v)!=10:
            raise ValueError("Phone number is not valid")