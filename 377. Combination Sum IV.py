from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        if target < 0:
            return 0
        res = 0
        for n in nums:
            res += self.combinationSum4(nums, target - n)
        return res

s = Solution()
nums = [1,2,3]
print(s.combinationSum4(nums, 4))
assert s.combinationSum4(nums, 4) == 7
