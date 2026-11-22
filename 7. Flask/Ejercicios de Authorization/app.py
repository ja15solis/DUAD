from flask import Flask, request, jsonify

from user_repository import user_repository
from product_repository import product_repository
from invoice_repository import invoice_repository, ProductDuplicateError, ProductNotFoundError, ProductNotAvailableError
from jwt_manager import JWTManager
from sqlalchemy.exc import IntegrityError
from pathlib import Path
from functools import wraps
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent

private_key_path = BASE_DIR / "private_key.pem"
public_key_path = BASE_DIR / "public_key.pem"

ACCESS_TOKEN_EXPIRATION = 60 * 15  # 15 minutos
REFRESH_TOKEN_EXPIRATION = 60 * 60 * 24 * 7  # 7 días

app = Flask("Fruit-store API")

jwt_manager = JWTManager(
    public_key=public_key_path.read_text(),
    private_key=private_key_path.read_text(),
    algorithm="RS256",
    access_expiration=ACCESS_TOKEN_EXPIRATION,
    refresh_expiration=REFRESH_TOKEN_EXPIRATION,
)
#user validation
def validate_token(func):
    @wraps(func) # This decorator keeps the original function's name and docstring intact, which is useful for debugging and documentation.
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token is None:
            return jsonify(error="Missing Authorization header"), 401
    
        token = token.replace("Bearer ", "")
        decoded = jwt_manager.decode_token(token, "access")
        if decoded is None:
            return jsonify(error="Invalid or expired access token please login again"), 401   
        
        user = user_repository.get_by_id(decoded["id"])
        if user is None:
            return jsonify(error="User not found please register"), 404
        
        return func(user_id = user.id, *args, **kwargs)
    return wrapper

def is_admin(func):
    @validate_token
    @wraps(func) 
    def wrapper(user_id,*args, **kwargs):
        user = user_repository.get_by_id(user_id)
        if not user.admin_user:
            return jsonify(error="Access denied, only admins can perform this action"), 403
        return func(user_id = user.id, *args, **kwargs)
    return wrapper

#body validation
def body_validation(body:dict,  fields, partial: bool = False) -> dict:
    if not body:
        raise ValueError("Missing JSON body.")

    allowed = set(fields)

    unexpected = body.keys() - allowed
    if unexpected:
        raise ValueError(f"Unexpected fields provided: {unexpected}")

    if not partial:
        missing = allowed - body.keys()
        if missing:
            raise ValueError(f"Missing required fields: {missing}")
    #for purchase the items must be a list of dictionaries with product_id and quantity, both positive integers
    if "items" in body:
        if not isinstance(body["items"], list):
            raise ValueError("'items' must be a list of dictionaries.")
        elif not body["items"]:
            raise ValueError("'items' list cannot be empty.")
        #loop through each item in the list and validate its structure and values
        for item in body["items"]:
            if not isinstance(item, dict):
                raise ValueError("Each item in 'items' must be a dictionary.")
            
            required_item_fields = {"product_id", "quantity"}
            missing_item_fields = required_item_fields - item.keys()
            unexpected_items = item.keys() - required_item_fields

            if unexpected_items:
                raise ValueError(f"Unexpected fields provided: {unexpected_items}")
                    
            if not partial:
                if missing_item_fields:
                    raise ValueError(f"Missing required fields: {missing_item_fields}")
            
            for field in ("quantity", "product_id"):
                if field in item:
                    value = item[field]
                    if isinstance(value, bool):
                        raise ValueError(f"'{field}' must be a number, not a boolean.")
                    if field in ("quantity", "product_id") and not isinstance(value, int):
                        raise ValueError(f"'{field}' must be an integer.")
                    if value < 1:
                        raise ValueError(f"'{field}' must be a positive number.")
        return body["items"]
                
    #for editing the product the price and quantity can be 0 but not negative, and name and date must be string
    else: 
        for field in ("price", "quantity"):
            if field in body:
                value = body[field]
                if isinstance(value, bool):
                    raise ValueError(f"'{field}' must be a number, not a boolean.")
                if field == "price" and not isinstance(value, (int, float)):
                    raise ValueError(f"'{field}' must be a number.")
                if field == "quantity" and not isinstance(value, int):
                    raise ValueError(f"'{field}' must be an integer.")
                if value < 0:
                    raise ValueError(f"'{field}' must be a non-negative number.")
        for field in ("name", "date"):
            if field in body:
                value = body[field]
                if not isinstance(value, str):
                    raise ValueError(f"'{field}' must be a string.")
                if field == "date":
                    try:
                        datetime.strptime(value, "%Y-%m-%d")
                    except ValueError:
                        raise ValueError(f"'{field}' must be in YYYY-MM-DD format.")

        for field, value in body.items():
            if value is None or (isinstance(value, str) and not value.strip()):
                raise ValueError(f"'{field}' must have a value.")

        return {k: body[k] for k in fields if k in body}

#Other functions
def serialize_product(product):
    return {
        "id": product.id,
        "name": product.name,
        "price": float(product.price),
        "quantity": product.quantity,
        "date": product.date.isoformat()
    }

def serialize_invoice(invoice):
    return {
        "id": invoice.id,
        "user_id": invoice.user_id,
        "amount": float(invoice.amount),
        "date": invoice.date.isoformat()
    }

#endpoints  
@app.route("/liveness")
def liveness():
    return jsonify(message="Service is running")

#User routes
@app.route("/register", methods=["POST"])
def register():
    try:
        data = body_validation(request.get_json(silent=True), ["username", "password"],partial=False)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    
    try:
        new_user = user_repository.create(data.get("username"), data.get("password"))
    except IntegrityError:
        return jsonify(error="Username already exists"), 409
    access_token, refresh_token = jwt_manager.generate_tokens(new_user.id)

    return jsonify(access_token=access_token, refresh_token=refresh_token), 201

@app.route("/login", methods=["POST"])
def login():
    try:
        data = body_validation(request.get_json(silent=True), ["username", "password"],partial=False)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    
    user = user_repository.get_by_credentials(data.get("username"), data.get("password"))
    if user is None:
        return jsonify(error="Invalid username or password"), 401

    access_token, refresh_token = jwt_manager.generate_tokens(user.id)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

@app.route("/me", methods=["GET"])
@validate_token
def me(user_id):
    user = user_repository.get_by_id(user_id)
    return jsonify(id=user.id, username=user.username)

@app.route("/refresh", methods=["POST"])
def refresh():
    try:
        data = body_validation(request.get_json(silent=True), ["refresh_token"],partial=False)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    
    refresh_token = data.get("refresh_token")

    decoded = jwt_manager.decode_token(refresh_token, "refresh")
    if decoded is None:
        return jsonify(error="Invalid or expired refresh token"), 401

    user = user_repository.get_by_id(decoded["id"])
    if user is None:
        return jsonify(error="User not found"), 404

    access_token, new_refresh_token = jwt_manager.generate_tokens(user.id)
    return jsonify(access_token=access_token, refresh_token=new_refresh_token),200

# Inventory routes
@app.route("/inventory", methods=["POST"])
@is_admin
def create_product(user_id):
    try:
        data = body_validation(request.get_json(silent=True), ["name","price", "quantity", "date"],partial=False)
    except ValueError as e:
        return jsonify(error=str(e)), 400

    product = product_repository.create(data.get("name"), data.get("price"), data.get("quantity"), data.get("date"))
    return jsonify(serialize_product(product)), 201

@app.route("/inventory/<int:product_id>", methods=["PATCH"])
@is_admin
def update_product(user_id, product_id):
    try:
        data = body_validation(request.get_json(silent=True), ["name", "price", "quantity", "date"],partial=True)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    
    rows = product_repository.modify(product_id, **data)
    if rows == 0:
        return jsonify(error="Product not found"), 404
    return jsonify(message="Product updated successfully"), 200

@app.route("/inventory/<int:product_id>", methods=["DELETE"])
@is_admin
def delete_product(user_id, product_id):
    rows = product_repository.delete(product_id)
    if rows == 0:
        return jsonify(error="Product not found"), 404
    return '', 204

@app.route("/inventory", methods=["GET"])
@validate_token
def list_products(user_id):
    products = product_repository.get_all()
    return jsonify([
        serialize_product(p)
        for p in products
    ]), 200

@app.route("/inventory/<int:product_id>", methods=["GET"])
@validate_token
def list_product(user_id, product_id):
    product = product_repository.get_by_id(product_id)
    if not product:
        return jsonify(error="Product not found"), 404
    return jsonify(serialize_product(product)), 200

@app.route("/invoices", methods=["GET"])
@validate_token
def list_invoices(user_id):
    invoices = invoice_repository.get_by_user_id(user_id)
    return jsonify([
        serialize_invoice(invoice)
        for invoice in invoices
    ]), 200

@app.route("/invoices", methods=["POST"])
@validate_token
def create_invoice(user_id):
    try:
        items = body_validation(request.get_json(silent=True), ["items"])
    except ValueError as e:
        return jsonify(error=str(e)), 400

    try:
        invoice = invoice_repository.create_purchase(user_id, items)
    except ProductNotFoundError as e:
        return jsonify(error=str(e)), 404
    except ProductNotAvailableError as e:
        return jsonify(error=str(e)), 409
    except ProductDuplicateError as e:
        return jsonify(error=str(e)), 400
    return jsonify(serialize_invoice(invoice)), 201


if __name__ == "__main__":
    app.run(debug=True)