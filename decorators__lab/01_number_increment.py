def number_increment(numbers):
    def increase():
        return [n + 1 for n in numbers]

    return increase()


print(number_increment([1, 2, 3]))


def increment_decorator(func):
    def wrapper(numbers):
        numbers = [n + 1 for n in numbers]
        return func(numbers)

    return wrapper


@increment_decorator
def number_increment(numbers):
    return numbers


print(number_increment([1, 2, 3]))
