def cache(func):

    # TODO: Implement
    def wrapper(number):
        if number not in wrapper.log.keys():
            wrapper.log[number] = func(number)
        return wrapper.log[number]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
print(fibonacci.log)
