from fastapi import status
from src.schemas.schema import AddUser, UpdateUser
from src.schemas.models import User
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


def add_user_api(data: AddUser, db: Session) -> JSONResponse:
    user_data = db.query(User).filter(User.email == data.email).first()

    if not user_data:
        try:
            new_user = User(
                username=data.username, email=data.email, project_id=data.project_id
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            content = new_user.__dict__
            del content["_sa_instance_state"]
            response = content
        except Exception as e:
            print(e)
            response = JSONResponse(
                content={
                    "msg": f"User with username : {data.username} allready exists"
                },
                status_code=status.HTTP_409_CONFLICT,
            )
    else:
        response = JSONResponse(
            content={"msg": f"User with email : {data.email} allready exists"},
            status_code=status.HTTP_409_CONFLICT,
        )

    return response


def get_user_api(user_id: int, db: Session) -> JSONResponse:

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return JSONResponse(
            content={"msg": f"User with id : {user_id} does not exsit"},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return user


def get_all_user_api(db: Session) -> JSONResponse:
    try:

        users = db.query(User).all()

        response = users
    except Exception as e:

        print(e)
        response = JSONResponse(
            content={"msg": "Exception Ocuures"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return response


def update_user_api(data: UpdateUser, db: Session):
    user = db.query(User).filter(User.id == data.id).first()
    if not user:
        response = JSONResponse(
            content={"msg": f"User with id : {data.id} does not exsit"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        try:
            if data.username is not None:
                user.username = data.username
            if data.email is not None:
                user.email = data.email
            if data.project_id is not None:
                user.project_id = data.project_id
            db.commit()
            db.refresh(user)
            response = user
        except Exception as e:
            response = JSONResponse(
                content={"msg": "Exception Ocuures"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    return response


def delete_user_api(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        response = JSONResponse(
            content={"msg": f"User with id : {user_id} does not exsit"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        try:
            db.delete(user)
            db.commit()
            response = JSONResponse(
                content={"msg": f"user {user.username} deleted"},
                status_code=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            response = JSONResponse(
                content={"msg": f"Exceptions Ocurres"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    return response
