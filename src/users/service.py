import sqlmodel

from fastapi import status, HTTPException

from sqlmodel.ext.asyncio.session import AsyncSession

from database.models import User

from auth.utils import hash_password

from .schemas import UserCreateSchema


async def get_user_by_id(id: int, db_session: AsyncSession) -> User:
    statement = sqlmodel.select(User).where(User.id == id)
    result = await db_session.exec(statement)
    await db_session.close()

    return result.first()


async def get_user_by_username(username: str, db_session: AsyncSession) -> User:
    statement = sqlmodel.select(User).where(User.username == username)
    result = await db_session.exec(statement)
    await db_session.close()

    return result.first()


async def add_user_to_db(
    new_user_credentials: UserCreateSchema, db_session: AsyncSession
) -> User:
    if await get_user_by_username(new_user_credentials.username, db_session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is unavailable",
        )

    new_user = User(**new_user_credentials.model_dump())
    new_user.hashed_password = hash_password(new_user_credentials.password)

    db_session.add(new_user)
    await db_session.commit()
    await db_session.close()

    return new_user
