from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True, unique=True, default=None)

    username: str = Field(unique=True, nullable=False, default=None)
    hashed_password: str = Field(nullable=False, default=None)
