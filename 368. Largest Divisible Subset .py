from collections import defaultdict
from typing import List

# score:  53%
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        nums.sort()
        n = len(nums)
        m = defaultdict(list)
        m[0] = [nums[0]]
        longestSet = m[0]
        for i in range(1, n):
            m[i] = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(m[j]) >= len(m[i]):
                    m[i] = m[j].copy() + [nums[i]]
            if len(m[i]) > len(longestSet):
                longestSet = m[i]

        return longestSet


s = Solution()
r = s.largestDivisibleSubset([1,2,4,8])
print(r)
assert r == [1,2,4,8]
r = s.largestDivisibleSubset([1,2,3])
print(r)
assert r == [1,2]
