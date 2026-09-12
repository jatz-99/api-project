
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from databases import get_db
from models import User as UserDB









class UserCreate(BaseModel):
    name: str
    age: int
    is_active: bool = True

@app.post("/users")
def create_user(user: UserCreate, db=Depends(get_db)):

    db_user = UserDB(
        name=user.name,
        age=user.age,
        is_active=user.is_active
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message": "User created successfully",
        "user_id": db_user.id,
        "name": db_user.name,
        "age": db_user.age,
        "is_active": db_user.is_active
    }


@app.get("/users/{user_id}")
def read_user(user_id: int, db=Depends(get_db)):

    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if user:
        return {
            "user_id": user.id,
            "name": user.name,
            "age": user.age,
            "is_active": user.is_active
        }

    return {"error": "User not found"}