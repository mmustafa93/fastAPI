"""add content column to posts table

Revision ID: 0006ffa4c933
Revises: 4e9705fc7d1f
Create Date: 2022-05-19 16:41:34.701755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0006ffa4c933'
down_revision = '4e9705fc7d1f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
