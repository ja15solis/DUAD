from src import models


def validate_movement(values, key_map, movement_type):
    #key map to return the value of a dict (the one with the desired input)
    try:
        title = values[key_map["title"]].strip()
        amount_input = values[key_map["amount"]].strip()
        category = values[key_map["category"]]
    except KeyError:
        return None, "Internal Error"

    if not title:
        return None, "Title" #returns no movement and the error
    if not amount_input:
        return None, "Amount"
    if not category:
        return None, "Category"
    try:
        amount = float(amount_input)
    except ValueError:
        return None, "Amount"
    if amount <= 0:
        return None, "Invalid Number"
    movement_data = {
        "movement_type": movement_type,
        "title": title,
        "amount": amount,
        "category": category
    }
    return models.Movement(**movement_data), None  #returns movement and no error