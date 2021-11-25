from typing import List
from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[nums[0], nums[0]]] # [max, min]

        i = 1
        res = nums[0]
        while i<l:
            pr_max, pr_min = dp[i-1][0], dp[i-1][1]
            dp.append([
                max(pr_max*nums[i], pr_min*nums[i], nums[i]),
                min(pr_max*nums[i], pr_min*nums[i], nums[i])
            ])
            res = max(res, dp[i][0], dp[i][1])
            i += 1

        return res


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.maxProduct([-2,0,-1])
print(r)
