from typing import List
from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def maxSubArray(self, nums: List[int]):
        l = len(nums)
        dp = []

        dp.append([0,0,nums[0]])
        i = 1
        res = nums[0]
        pos = [0,0]
        while i<l:
            last = i-1
            if dp[last][2] < 0:
                dp.append([i, i, nums[i]])
            else:
                dp.append([dp[last][0], i, nums[i] + dp[last][2]])
            if dp[i][2] >= res:
                res = dp[i][2]
                pos = dp[i][:2]
            i += 1

        return res, pos



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(r)
