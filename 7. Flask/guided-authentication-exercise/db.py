from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

DB_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DB_URI)

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(30), unique=True, nullable=False),
    Column("password", String, nullable=False),
)

metadata_obj.create_all(engine)