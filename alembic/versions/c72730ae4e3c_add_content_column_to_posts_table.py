"""add content column to posts table

Revision ID: c72730ae4e3c
Revises: 78c5b0d22531
Create Date: 2023-10-09 22:51:51.553821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c72730ae4e3c'
down_revision: Union[str, None] = '78c5b0d22531'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
