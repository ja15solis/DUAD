from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import select

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

metadata_obj = MetaData()

user_table = Table(
		"users",
		metadata_obj,
		Column("id", Integer, primary_key=True),
		Column("name", String(30)),
		Column("fullname", String),
)


address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id"), nullable=False), #De esta manera declaramos una FK
    Column("email_address", String, nullable=False),
)

# metadata_obj.create_all(engine, checkfirst=True)

# with engine.connect() as conn:
#     result = conn.execute(
#         insert(user_table),
#         [
#             {"name": "sandy", "fullname": "Sandy Cheeks"},
#             {"name": "patrick", "fullname": "Patrick Star"},
#         ],
#     )
#     conn.commit()

# from sqlalchemy import insert

# stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()

from sqlalchemy import select

stmt = select(user_table).where(user_table.c.name == "spongebob")


with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row)