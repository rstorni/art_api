"""empty message

Revision ID: 5a07584345b9
Revises: d60e46894493
Create Date: 2024-12-26 17:50:42.805802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a07584345b9'
down_revision: Union[str, None] = 'd60e46894493'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
