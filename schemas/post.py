from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title:str 
    content:str

class PostUpdate(BaseModel):
    title:str
    content:str

class PostRead(BaseModel):
    id:int
    title:str
    content:str
    created_at:datetime
    updated_at:datetime

    class Config:
        orm_mode = True