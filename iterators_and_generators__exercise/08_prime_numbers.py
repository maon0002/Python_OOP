from typing import List


def get_primes(nums: List[int]):
    for n in nums:
        if n <= 1:
            continue

        for divider in range(2, n):
            if n % divider == 0:
                break
        else:
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
