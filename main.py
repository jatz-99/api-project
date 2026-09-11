from pydantic import BaseModel
from fastapi import FastAPI  
app = FastAPI()
fake_db = {}
@app.get("/fa/{no}")
def fa (no:int):
    result=1
    for i in range(1, no+1):
        result = result * i
    return result



user_id = int


class user(BaseModel):
  name: str
  age: int
  is_active: bool = True


@app.post("/greet")
def greet_user(user: user, user_id: int):
    return {"user_id": int ,"message": "user created", "name": User.name, "age": User.age, "is_active": User.is_active}



