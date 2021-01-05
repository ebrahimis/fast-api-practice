"""adding column

Revision ID: 78d1406500b3
Revises: a86e53f9cce0
Create Date: 2021-01-05 14:34:15.699368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78d1406500b3'
down_revision = 'a86e53f9cce0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('test_column', sa.String()))


def downgrade():
    op.drop_column('users', 'test_column')
