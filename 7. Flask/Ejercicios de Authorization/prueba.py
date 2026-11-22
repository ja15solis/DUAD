from app import body_validation

request = {
    "items" : 
        [
            {"product_id": 1,"quantity": 2},
            {"product_id": 2,"quantity": 2}
        ] 
}
print(body_validation(request, ["items"]))