from typing import Annotated

from fastapi import APIRouter, Depends

from sqlmodel.ext.asyncio.session import AsyncSession

from database.models import User
from database.session import get_db_session

from .schemas import UserCreateSchema
from .service import add_user_to_db


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", response_model=User)
async def create_user(
    user_credentials: UserCreateSchema,
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
) -> User:
    return await add_user_to_db(user_credentials, db_session)
