from itertools import permutations


def possible_permutations(seq):
    for el in permutations(seq):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
