from fastapi import FastAPI
from database import Base, engine
from auth import auth_router

app = FastAPI()
app.include_router(auth_router, prefix='/auth', tags=['auth'])

Base.metadata.create_all(bind=engine)
