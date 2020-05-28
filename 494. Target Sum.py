from collections import defaultdict
from typing import List


# dp[elem #][target] -> possibilities
# dp[i][j] -> dp[i+1][j+v(i+1)]
# dp[i][j] -> dp[i+1][j-v(i+1)]
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int):
        g = defaultdict(lambda: defaultdict(int))
        g[-1][0] = 1
        for i in range(len(nums)):
            v = nums[i]
            for old in g[i-1]:
                g[i][old+v] += g[i-1][old]
                g[i][old-v] += g[i-1][old]

        return g[len(nums)-1][S]

s = Solution()
nums = [1,1,1,1,1]
assert s.findTargetSumWays(nums, 3)==5
assert s.findTargetSumWays(nums, -2)==0



