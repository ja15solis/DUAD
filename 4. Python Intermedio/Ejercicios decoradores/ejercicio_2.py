
def check_number(func):
    def wrapper(*args):
        try:
            new_args = list(map(float, args))  #trying to convert every value to float
            return func(*new_args) #asterisk to unpack the list of arguments
        except (ValueError,TypeError):
                raise ValueError("All parameters must be numbers")
    return wrapper

@check_number
def get_max_number(*args):
    return max(args)


print("-" * 47)
print("Example without error:")
print(" - " * 16)
number = get_max_number(1231,2234,23,4234,545)
print(number)

print("-" * 47)
print("Example without error:")
print(" - " * 16)
number = get_max_number(1231,2234,23,"4234",545)
print(number)

print("-" * 47)
print("Example with error:")
print(" - " * 16)
number = get_max_number(1231,2234,"23c",4234,545)
print(number)