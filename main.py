from pydantic import BaseModel
from fastapi import FastAPI  
app = FastAPI()
print("THIS IS THE FILE I AM RUNNING")
# @app.get("/fa/{no}")
# def fa (no:int):
#     result=1
#     for i in range(1, no+1):
#         result = result * i
#     return result






class User(BaseModel):
  name: str
  age: int
  is_active: bool = True


@app.post("/greet")
def greet_user(User: User):
    return {"message": "user created", "name": User.name, "age": User.age, "is_active": User.is_active}



