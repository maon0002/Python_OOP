# class vowels:
#     # match = ['a', 'e', 'i', 'u', 'y', 'o']
#
#     def __init__(self, txt: str):
#         self.txt = txt
#         self.start = 0
#         self.end = len(self.txt) + 1
#         self.match = match = ['a', 'e', 'i', 'u', 'y', 'o']
#
#     # def __iter__(self):
#     #     return (ch for ch in self.txt if ch.lower() in vowels.match)
#
#     def __iter__(self):
#         return (ch for ch in self.txt if ch.lower() in self.match)
#
#     def __next__(self):
#
#         if self.start <= self.end:
#             curr_char = self.txt[self.start]
#             yield curr_char
#             self.start += 1
#         else:
#             raise StopIteration()
#
#
#
# my_string = vowels('Abcedifuty0o')
# # my_string = vowels('AEYUIO1234567890')
# for char in my_string:
#     print(char)


#
# class vowels:
#
#     def __init__(self, txt: str):
#         self.txt = txt
#         self.idx = len(self.txt)
#
#     def __iter__(self):
#         return iter(x for x in self.txt if x in ['a', 'e', 'i', 'u', 'y', 'o'])
#
#     def __next__(self):
#         if self.idx > 0:
#
#             # if self.txt[self.idx] in ['a', 'e', 'i', 'u', 'y', 'o']:
#             yield self.txt[self.idx]
#             self.idx -= 1
#         else:
#             raise StopIteration()

# my_string = vowels('Abcedifuty0o')
# # my_string = vowels('AEYUIO1234567890')
# for char in my_string:
#     print(char)



# class vowels:
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#         self.vowels = set('aeiouAEIOU')
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.string):
#             char = self.string[self.index]
#             self.index += 1
#             if char in self.vowels:
#                 return char
#         raise StopIteration
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


class vowels:

    def __init__(self, txt: str):
        self.txt = txt
        self.idx = len(self.txt)
        self.valid_chars = ['a', 'e', 'i', 'u', 'y', 'o']

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(0, self.idx):
            char = self.txt[i]
            if char.lower() in self.valid_chars:
                return char
            if i >= self.idx:
                raise StopIteration






my_string = vowels('Abcedifuty0o')
# my_string = vowels('AEYUIO')
for char in my_string:
    print(char)

# while self.index < len(self.string):
#     char = self.string[self.index]
#     self.index += 1
#     if char in self.vowels:
#         return char
# raise StopIteration