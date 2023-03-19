def reverse_text(txt):
    # reversed_txt = reversed(txt)
    # for ch in reversed_txt:
    #     yield ch

    for ch in txt[::-1]:
        yield ch


for char in reverse_text("step"):
    print(char, end='')



# class reverse_text:
#
#     def __init__(self, txt):
#         self.txt = txt
#
#     def __iter__(self):
#         return (ch for ch in self.txt[::-1])
#
#     def __next__(self):
#         if self.txt[]
#
# for char in reverse_text("step"):
#     print(char, end='')

# def genrange(start, end):
#     i = start
#     n = end
#     while i <= n:
#         yield i
#         i += 1
#
# class reverse_text: