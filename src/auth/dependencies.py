from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer

from sqlalchemy.ext.asyncio.session import AsyncSession

from database.session import get_db_session
from database.models import User

from users.service import get_user_by_id

from .utils import decode_token

access_token_bearer = HTTPBearer(description="Access token bearer")


async def get_current_user(
    bearer: Annotated[str, Depends(access_token_bearer)],
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
) -> User:
    token_data: dict = decode_token(bearer.credentials)

    return await get_user_by_id(int(token_data["sub"]), db_session)
