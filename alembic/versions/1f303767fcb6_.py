"""empty message

Revision ID: 1f303767fcb6
Revises: 311c5d7af064
Create Date: 2024-12-28 12:06:38.356214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f303767fcb6'
down_revision: Union[str, None] = '311c5d7af064'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
