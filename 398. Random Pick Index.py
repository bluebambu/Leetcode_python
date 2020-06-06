import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        res = -1
        for idx, i in enumerate(self.nums):
            if i == target:
                cnt += 1
                if random.randint(1, cnt) == 1:
                    res = idx

        return res

# Your Solution object will be instantiated and called as such:
nums = [1,2,3,3,3]
obj = Solution(nums)
param_1 = obj.pick(3)
print(param_1)
param_1 = obj.pick(3)
print(param_1)
param_1 = obj.pick(3)
print(param_1)
