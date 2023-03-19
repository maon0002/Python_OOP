class reverse_iter:

    def __init__(self, nums: list):
        self.nums = nums
        self.idx = len(self.nums)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > 0:
            self.idx -= 1
            return self.nums[self.idx]
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
