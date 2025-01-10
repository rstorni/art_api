"""empty message

Revision ID: 0b710037f6c9
Revises: 1f303767fcb6
Create Date: 2024-12-28 18:39:03.980209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b710037f6c9'
down_revision: Union[str, None] = '1f303767fcb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
