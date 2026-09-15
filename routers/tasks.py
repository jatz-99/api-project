
from fastapi import Depends, APIRouter
from pydantic import BaseModel, ConfigDict
from databases import get_db
from models import User as UserDB, post as Post_db



router = APIRouter(prefix="/users", tags=["users"]) 


class PostBase(BaseModel):
    title: str
    description: str
    user_id: int
class PostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    model_config = ConfigDict(from_attributes=True)


@router.post("/{user_id}/tasks")
def create_task_for_user(user_id: int, task: PostBase, db=Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if user is not None:
        db_task = Post_db(
            title=task.title,
            description=task.description,
            user_id=user_id
        )

        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return {
            "message": "Task created successfully",
            "task_id": db_task.id,
            "title": db_task.title,
            "description": db_task.description,
            "user_id": db_task.user_id
        }
    return {"error": "User not found"}
