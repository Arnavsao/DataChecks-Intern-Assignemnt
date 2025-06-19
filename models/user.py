from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"
    id  = Column(Integer, primary_key=True,index=True)
    title = Column(String, nullable=False)
    content = Column(String,nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updates_at = Column(DateTime(timezone=True), onupdate=func.now())

