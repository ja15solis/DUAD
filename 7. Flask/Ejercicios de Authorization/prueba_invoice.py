from invoice_repository import invoice_repository

print(invoice_repository.create_purchase(1, [{"product_id": 1, "quantity": 2}]))   # factura creada
print(invoice_repository.create_purchase(1, [{"product_id": 99, "quantity": 1}]))  # producto no existe
print(invoice_repository.create_purchase(1, [{"product_id": 1, "quantity": 9999}]))  # sin stock