from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    expires_at: int
    token_type: str = "bearer"
