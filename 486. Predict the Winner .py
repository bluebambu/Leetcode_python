from collections import defaultdict
from typing import List

# score: 50%
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        def win(nums: List):
            h = str(nums)
            if h in m:
                return m[h]

            if len(nums) == 1:
                return nums[0]

            r1 = nums[0] - win(nums[1:])
            r2 = nums[-1] - win(nums[:-1])
            m[h] = max(r1, r2)
            return max(r1, r2)

        return win(nums) >= 0


s = Solution()
r = s.PredictTheWinner([1,5,2])
print(r)
assert r == False
