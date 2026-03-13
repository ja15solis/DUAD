
def check_number(func):
    def wrapper(*args):
        try:
            for arg in args:
                float(arg)
            print(f"Parameters: {args}")
            result = func(*args)
            print(f"The max number in the parameters is: {result}")
        except (ValueError,TypeError):
                return "There is a parameter that is not a number"
    return wrapper

@check_number
def get_max_number(*args):
    return max([float(arg) for arg in args])


print("-" * 47)
print("Example without error:")
print(" - " * 16)
number = get_max_number(1231,2234,23,4234,545)

print("-" * 47)
print("Example without error:")
print(" - " * 16)
number = get_max_number(1231,2234,23,"4234",545)

print("-" * 47)
print("Example with error:")
print(" - " * 16)
print(get_max_number(1231,2234,"23c",4234,545))