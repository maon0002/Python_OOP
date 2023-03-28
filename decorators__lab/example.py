def my_decorator(func):
    def wrapper():
        print("Before the function say_hello is called")
        func()
        print("After the function say_hello is called")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()
