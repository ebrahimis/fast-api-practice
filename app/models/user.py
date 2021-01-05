from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Users(BaseModel):
    """
    Model contain users data.

    :param id: A unique id that identifies user.
    :param email: User email.
    :param name: User name.
    :param hashed_password: User password.
    """
    id: Optional[UUID]
    name: str
    hashed_password: str
    email: str
    is_active: bool


    class Config:
        orm_mode = True
