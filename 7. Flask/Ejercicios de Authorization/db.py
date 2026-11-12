from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Numeric, create_engine, MetaData, Table, Column, Integer, String, Boolean, Date

DB_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DB_URI)

metadata_obj = MetaData()

user_table = Table(
    "app_users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("admin_user", Boolean, nullable=False),
    Column("username", String(30), unique=True, nullable=False),
    Column("password", String, nullable=False),
)

inventory_table = Table(
    "app_inventory",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("price", Numeric(10, 2), nullable=False),
    Column("date", Date, nullable=False),
    Column("quantity", Integer, CheckConstraint("quantity>=0"), nullable=False),
)

invoice_table = Table(
    "app_invoice",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("app_users.id"), nullable=False),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("date", DateTime, nullable=False),
)

invoice_details_table = Table(
    "app_invoice_details",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("invoice_id", Integer, ForeignKey("app_invoice.id"), nullable=False),
    Column("product_id", Integer, ForeignKey("app_inventory.id", ondelete="SET NULL"), nullable=True),
    Column("product_name", String(100), nullable=False),
    Column("quantity", Integer, CheckConstraint("quantity>=1"), nullable=False),
    Column("price", Numeric(10, 2), nullable=False),
)

metadata_obj.create_all(engine, checkfirst=True)