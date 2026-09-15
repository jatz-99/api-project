from fastapi import Depends, APIRouter
from pydantic import BaseModel, ConfigDict

from databases import get_db, engine
from models import User as UserDB
from tasks import PostResponse



router = APIRouter(prefix="/users", tags=["users"])



class UserCreate (BaseModel):
    name: str
    age: int
    is_active: bool = True
class UserResponse (BaseModel):
    id: int 
    name: str
    age: int
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
    tasks: list[PostResponse]


@router.post("/")
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



@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db=Depends(get_db)):

    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if user:
       return user

    return {"error": "User not found"}