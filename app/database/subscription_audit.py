from app.database.database import metadata
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, SmallInteger, String, Table, JSON


subscription_audit = Table(
    'subscription_audit',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('subscription_id', UUID(as_uuid=True), ForeignKey('subscriptions.id'), nullable=False, index=True),
    Column('event_type', SmallInteger, nullable=False),
    Column('event', JSON),
    Column('updated_by', UUID(as_uuid=True))
)
