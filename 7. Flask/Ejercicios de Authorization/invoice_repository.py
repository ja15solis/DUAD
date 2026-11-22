from sqlalchemy import  func, insert, select
from db import engine, invoice_table, invoice_details_table, inventory_table
from collections import Counter

#identifier for custom exceptions
class ProductNotFoundError(Exception):
    pass
class ProductNotAvailableError(Exception):
    pass
class ProductDuplicateError(Exception):
    pass

class InvoiceRepository:
    def __init__(self, engine):
        self.engine = engine

    def create_purchase(self, user_id, items: list):
        counter = Counter(i['product_id'] for i in items)
        duplicate_items = [k for k, cantidad in counter.items() if cantidad > 1]
                    
        if duplicate_items:
            raise ProductDuplicateError(f"These product_id are duplicated: {duplicate_items}")
        
        with self.engine.begin() as conn:
            
            
            invoice_stmt = (
                insert(invoice_table)
                .values(user_id=user_id, amount= 0 , date=func.now())
                .returning(invoice_table.c.id, invoice_table.c.user_id, invoice_table.c.amount, invoice_table.c.date)
            )
            invoice_id = conn.execute(invoice_stmt).first().id


            for item in items:
                product = conn.execute(select(inventory_table).where(inventory_table.c.id == item['product_id'])).first()
                if not product:
                    raise ProductNotFoundError(f"Product with id {item['product_id']} not found")
                quantity = product.quantity
                if quantity < item['quantity']:
                    raise ProductNotAvailableError(f"Not enough quantity for product_id {item['product_id']}. Available: {quantity}, Requested: {item['quantity']}")
                change_quantity_stmt = (
                    inventory_table.update()
                    .where(inventory_table.c.id == item['product_id'])
                    .values(quantity=inventory_table.c.quantity - item['quantity'])
                )

                conn.execute(change_quantity_stmt)

                invoice_details_stmt = insert(invoice_details_table).values(
                    invoice_id=invoice_id,
                    product_id=item['product_id'],
                    product_name=inventory_table.select().where(inventory_table.c.id == item['product_id']).with_only_columns(inventory_table.c.name).scalar_subquery(),
                    quantity=item['quantity'],
                    price= inventory_table.select().where(inventory_table.c.id == item['product_id']).with_only_columns(inventory_table.c.price).scalar_subquery(),
                )
                
                conn.execute(invoice_details_stmt)

            result = conn.execute(
                invoice_table.update()
                .where(invoice_table.c.id == invoice_id)
                .values(amount=select(func.sum(invoice_details_table.c.price * invoice_details_table.c.quantity)).where(invoice_details_table.c.invoice_id == invoice_id).scalar_subquery())
                .returning(invoice_table.c.id, invoice_table.c.user_id, invoice_table.c.amount, invoice_table.c.date)
            )
            return result.first()

    def get_by_user_id(self, user_id):
        stmt = select(invoice_table).where(invoice_table.c.user_id == user_id).order_by(invoice_table.c.date.desc())
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.fetchall()


invoice_repository = InvoiceRepository(engine)