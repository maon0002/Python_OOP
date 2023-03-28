class store_results:

    def __init__(self, arg):
        self.arg = arg

    def __call__(self, func):
        def wrapper(*args):
            print(f"Function {func.__name__} was called. Result: {func(*args)}")
            print("The argument is", self.arg)

        return wrapper


@store_results(6)
def add(a, b):
    return a + b


@store_results(5)
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
