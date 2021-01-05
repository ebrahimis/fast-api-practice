"""create tables

Revision ID: aa29ae034b22
Revises: 
Create Date: 2020-12-29 14:52:38.050067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'aa29ae034b22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', UUID, primary_key=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True)
    )

    op.create_table(
        'subscriptions',
        sa.Column('id', UUID, primary_key=True, index=True),
        sa.Column('client_id', UUID, nullable=False),
        sa.Column('offer_id', UUID, nullable=False),
        sa.Column('offer_instance_id', UUID, nullable=False),
        sa.Column('client_id', UUID, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('is_gift', sa.Boolean, nullable=False),
        sa.Column('begin_date', sa.DateTime),
        sa.Column('end_date', sa.DateTime, index=True),
        sa.Column('is_trial', sa.Boolean, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('num_trials', sa.SmallInteger, nullable=False),
        sa.Column('is_auto_renew', sa.Boolean, nullable=False),
        sa.Column('last_renew_date', sa.DateTime),
        sa.Column('next_renew_date', sa.DateTime, index=True),
        sa.Column('status_id', sa.SmallInteger, nullable=False)
    )

    op.create_table(
        'subscription_audit',
        sa.Column('id', UUID, primary_key=True, index=True),
        sa.Column('subscription_id', UUID, sa.ForeignKey('subscriptions.id'), index=True, nullable=False),
        sa.Column('event_type', sa.SmallInteger, nullable=False),
        sa.Column('event', sa.JSON),
        sa.Column('updated_by', sa.Text)
    )


def downgrade():
    op.drop_table('subscription_audit')
    op.drop_table('subscriptions')
    op.drop_table('users')
