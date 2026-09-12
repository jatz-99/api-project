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


class user(BaseModel):
  name: str
  age: int
  is_active: bool = True


@app.post("/greet")
def greet_user(user: user, user_id: int):
    fake_db[user_id] = user
    return {"user_id":user_id ,"message": "user created", "name": user.name, "age": user.age, "is_active": user.is_active}

@app.get("/get_user/{user_id}")
def get_user(user_id: int):
    user = fake_db.get(user_id)
    if user:
        return {"user_id": user_id, "name": user.name, "age": user.age, "is_active": user.is_active}
    else:
        return {"error": "User not found"}

@app.put("/update_user/{user_id}")
def update_user(user_id: int, updated_user: user):
    if user_id in fake_db:
        fake_db[user_id] = updated_user
        return {"user_id": user_id, "message": "User updated", "name": updated_user.name, "age": updated_user.age, "is_active": updated_user.is_active}
    else:
        return {"error": "User not found"}

    
@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    if user_id in fake_db:
        del fake_db[user_id]
        return {"user_id": user_id, "message": "User deleted"}
    else:
        return {"error": "User not found"}
