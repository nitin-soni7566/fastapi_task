from fastapi import Body
from pydantic import EmailStr
from enum import Enum


class ProjectID(int, Enum):
    a = 1
    b = 2
    c = 3


class AddUser:

    def __init__(
        self,
        username: str = Body(description="Unique username"),
        email: EmailStr = Body(description="User email address"),
        project_id: ProjectID = Body(description="Project id 1,2,3"),
    ):

        self.username = username
        self.email = email
        self.project_id = project_id


class UpdateUser:

    def __init__(
        self,
        id: int = Body(description="Existing user id"),
        username: str = Body(description="Unique username"),
        email: EmailStr = Body(description="User email address"),
        project_id: ProjectID = Body(description="Project id 1,2,3"),
    ):

        self.id = id
        self.username = username
        self.email = email
        self.project_id = project_id
