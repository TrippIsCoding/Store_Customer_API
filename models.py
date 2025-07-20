from database import Base
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    '''
    the UserModel class is inheriting from database.py Base class to create database tables for users
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)
    email = Column(String, index=True, unique=True)
    full_name = Column(String, nullable=True)
    address = Column(String)
    phone_number = Column(String)


class User(BaseModel):
    '''
    the User class is inheriting from pydantic BaseModel for validation
    '''
    username: Annotated[str, Field(min_length=3, max_length=20)]
    password: Annotated[str, Field(min_length=8, max_length=72)]
    email: Annotated[str, Field(max_length=100)]
    full_name: Annotated[str, Field(max_length=100)] | None = None
    address: Annotated[str, Field(min_length=5, max_length=250)]
    phone_number: Annotated[str, Field(min_length=10, max_length=10)]

    class Config:
        from_attributes = True