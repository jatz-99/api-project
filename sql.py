
from fastapi import FastAPI
from databases import engine
from models import Base
Base.metadata.create_all(bind=engine)
from routers import users
from routers import tasks

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)







