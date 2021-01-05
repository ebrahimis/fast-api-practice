from app.database.database import metadata
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, SmallInteger, String, Table
import sqlalchemy as sa


subscriptions = Table(
    'subscriptions',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, index=True),
    Column('client_id', UUID(as_uuid=True), nullable=False),
    Column('offer_id', UUID(as_uuid=True), nullable=False),
    Column('offer_instance_id', UUID(as_uuid=True), nullable=False),
    Column('purchaser_id', UUID(as_uuid=True), ForeignKey('users.id'), nullable=False),
    Column('is_gift', Boolean, nullable=False),
    Column('begin_date', DateTime),
    Column('end_date', DateTime, index=True),
    Column('is_trial', Boolean, nullable=False),
    Column('num_trials', SmallInteger, nullable=False),
    Column('is_auto_renew', Boolean, nullable=False),
    Column('last_renew_date', DateTime),
    Column('next_renew_date', DateTime, index=True),
    Column('status_id', SmallInteger),
    Column('updated_at', DateTime, nullable=False, onupdate=datetime.utcnow,
                         default=datetime.utcnow, server_default=sa.func.now())
)
