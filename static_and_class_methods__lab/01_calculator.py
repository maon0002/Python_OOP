from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*nums: List[int]) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums: List[int]):
        return reduce(lambda a, b: a * b, nums)

    @staticmethod
    def divide(*nums: List[int]) -> int:
        return reduce(lambda a, b: a / b, nums)

    @staticmethod
    def subtract(*nums):
        return reduce(lambda a, b: a - b, nums)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))