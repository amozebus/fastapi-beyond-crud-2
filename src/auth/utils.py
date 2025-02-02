import time

from fastapi import HTTPException, status

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from passlib.context import CryptContext

from config import settings

from database.models import User


crypt_context: CryptContext = CryptContext(schemes=["bcrypt"])


def hash_password(plain_password: str) -> str:
    return crypt_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return crypt_context.verify(plain_password, hashed_password)


def create_access_token(user: User) -> str:
    expire: int = settings.ACCESS_TOKEN_EXPIRE

    claims = {
        "sub": str(user.id),
        "iat": int(time.time()),
        "exp": int(time.time()) + expire
    }

    return jwt.encode(
        headers={"alg": "HS256", "typ": "JWT"},
        payload=claims,
        key=settings.JWT_SECRET,
    )


def decode_token(token: str) -> dict:
    try:
        token_data: dict = jwt.decode(
            jwt=token, key=settings.JWT_SECRET, algorithms=["HS256"]
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired token"
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    return token_data
