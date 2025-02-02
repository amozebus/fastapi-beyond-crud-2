"""create_users_table

Revision ID: 68a1cb378cd9
Revises:
Create Date: 2025-01-30 07:06:30.553767

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68a1cb378cd9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.INTEGER,
            primary_key=True,
            unique=True,
            nullable=False,
            default=None,
        ),
        sa.Column("username", sa.VARCHAR, unique=True, nullable=False, default=None),
        sa.Column("hashed_password", sa.VARCHAR, nullable=False, default=None),
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_table("users", if_exists=True)
