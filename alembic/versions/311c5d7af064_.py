"""empty message

Revision ID: 311c5d7af064
Revises: c00200345d92
Create Date: 2024-12-28 11:44:24.584963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '311c5d7af064'
down_revision: Union[str, None] = 'c00200345d92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
