from fastapi import APIRouter, Depends
from src.controllers.user_serviecs import (
    add_user_api,
    get_user_api,
    delete_user_api,
    update_user_api,
    get_all_user_api,
)
from src.schemas.schema import AddUser, UpdateUser
from sqlalchemy.orm import Session
from src.database.connect import get_db


router = APIRouter(tags=["User"])


@router.post("/add_users", status_code=201)
def add_user(payload: AddUser = Depends(), db: Session = Depends(get_db)):
    """This function add new user for project_ids

    Args:
        payload (AddUser, optional): _description_. Defaults to Depends().
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        Json: return's user details with id
    """

    return add_user_api(payload, db)


@router.get("/get_users/{id}", status_code=200)
def get_user(id: int, db: Session = Depends(get_db)):
    """This api for get user details

    Args:
        id (int): existing user id

    Returns:
        Json: This function will reuturn user details
    """
    return get_user_api(id, db)


@router.get("/get_users", status_code=200)
def get_all_user(db: Session = Depends(get_db)):
    """This api for get user details

    Args:
        id (int): existing user id

    Returns:
        Json: This function will reuturn user details
    """
    return get_all_user_api(db=db)


@router.patch("/update_users")
def update_user(data: UpdateUser = Depends(), db: Session = Depends(get_db)):
    """This functions will update user details

    Args:
        data (UpdateUser, optional): _description_. Defaults to Depends().

    Returns:
        Json: This will return updated user details
    """
    return update_user_api(data, db)


@router.delete("/delete_users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    """This function delete user from database

    Args:
        id (int): existing user id

    Returns:
        Json: string msg
    """
    return delete_user_api(id, db)
