from src.database.base import Base
from sqlalchemy import Integer, Column, String, DateTime
from datetime import datetime


class User(Base):

    __tablename__ = "usertable"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    project_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{{'id': {self.id}, 'username': {self.username}, 'email': {self.email}, 'project_id': {self.project_id}, 'created_at': {self.created_at}}}"
