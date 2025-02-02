from typing import Annotated

from fastapi import APIRouter, Depends

from database.models import User

from auth.dependencies import get_current_user

router = APIRouter(tags=["Routes examples"])


@router.get("/unprotected", response_model=dict)
async def unprotected_endpoint_example() -> dict:
    return {"message": "Hello, world!"}


@router.get("/protected", response_model=dict)
async def protected_endpoint_example(
    current_user: Annotated[User, Depends(get_current_user)],
) -> dict:
    return {"message": "Hello, world!", "current_user": current_user}
