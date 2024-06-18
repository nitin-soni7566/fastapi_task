from fastapi import APIRouter, Depends

router = APIRouter(tags=["Home"])


@router.get("/")
def home():
    """This is home route

    Returns:
        _type_: string
    """
    return {"message": "Home route"}
