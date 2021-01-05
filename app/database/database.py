from app.settings.config import get_database_url
from sqlalchemy import create_engine, MetaData
import sqlalchemy as sa


SQLALCHEMY_DATABASE_URL = get_database_url()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

metadata = MetaData()
metadata.bind = engine
