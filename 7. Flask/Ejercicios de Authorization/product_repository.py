from sqlalchemy import  insert, select
from db import engine, inventory_table


class ProductRepository:
    def __init__(self, engine):
        self.engine = engine

    def create(self, name, price, quantity, date):
        stmt = (
            insert(inventory_table)
            .values(name=name, price=price, quantity=quantity, date=date)
            .returning(inventory_table.c.id, inventory_table.c.name, inventory_table.c.price, inventory_table.c.quantity, inventory_table.c.date)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.first()

    def modify(self, product_id, **kwargs):
        stmt = (
            inventory_table.update()
            .where(inventory_table.c.id == product_id)
            .values(**kwargs)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.rowcount

    def delete(self, product_id):
        stmt = (
            inventory_table.delete()
            .where(inventory_table.c.id == product_id)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.rowcount

    def get_by_id(self, product_id):
        stmt = select(inventory_table).where(inventory_table.c.id == product_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.first()

    def get_all(self):
        stmt = select(inventory_table)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.fetchall()


product_repository = ProductRepository(engine)