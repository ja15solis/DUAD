
def print_params(func):
    def wrapper(*args):
        print(f"Parameters: {args}")
        result = func(*args)
        print(f"The max number in the parameters is: {result}")
    return wrapper

@print_params
def get_max_number(*args):
    max_number = max(args)
    return max_number


number = get_max_number(1231,2234,3342,4234,545)
