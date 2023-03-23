class sequence_repeat:
    def __init__(self, seq, num: int):
        self.seq = seq
        self.num = num
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.num - 1:
            raise StopIteration

        self.idx += 1

        return self.seq[self.idx % len(self.seq)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
