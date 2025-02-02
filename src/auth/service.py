import fastapi

from fastapi import HTTPException

from sqlmodel.ext.asyncio.session import AsyncSession

from database.models import User

from users.service import get_user_by_username

from .schemas import LoginSchema
from .utils import verify_password


async def authenticate_user(
    user_credentials: LoginSchema, db_session: AsyncSession
) -> User:
    user = await get_user_by_username(user_credentials.username, db_session)
    if user:
        if verify_password(user_credentials.password, user.hashed_password):
            return user
    raise HTTPException(
        status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
    )
