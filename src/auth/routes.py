import time

from typing import Annotated

from fastapi import APIRouter, Depends

from sqlmodel.ext.asyncio.session import AsyncSession

from config import settings

from database.models import User
from database.session import get_db_session

from .schemas import LoginSchema, TokenSchema
from .service import authenticate_user
from .utils import create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/token", response_model=TokenSchema)
async def get_access_token(
    user_credentials: LoginSchema,
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
) -> TokenSchema:
    user: User = await authenticate_user(user_credentials, db_session)

    return TokenSchema(
        access_token=create_access_token(user),
        expires_at=int(time.time() + settings.ACCESS_TOKEN_EXPIRE * 60),
    )
