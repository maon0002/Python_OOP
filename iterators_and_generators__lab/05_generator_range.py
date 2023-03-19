def genrange(start, end):
    for i in range(start, end + 1):
        yield i


print(list(genrange(1, 10)))


# def genrange(start, end):
#     i = start
#     n = end
#     while i <= n:
#         yield i
#         i += 1
