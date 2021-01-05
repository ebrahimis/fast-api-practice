from app.database.database import metadata
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, String, Table


users = Table(
    'users',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('email', String, unique=True, index=True, nullable=False),
    Column('name', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, nullable=False, default=True)
)
