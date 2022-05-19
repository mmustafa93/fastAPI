"""add last few columns to posts table

Revision ID: e8e260d11579
Revises: df9f324b16a4
Create Date: 2022-05-19 17:27:22.911043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8e260d11579'
down_revision = 'df9f324b16a4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts', sa.Column('published', sa.Boolean(), nullable=False
        , server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False
        , server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
