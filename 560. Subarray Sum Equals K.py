from typing import List
from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        dp = [0]
        for n in nums:
            dp.append(n + dp[-1])

        thru_sum = {0: [-1]}
        res = 0

        for i, num in enumerate(nums):
            sum = dp[i+1]
            tgt = sum - k
            matchedList = thru_sum.get(tgt)
            if matchedList is not None:
                res += len(matchedList)
            f = thru_sum.get(sum, [])
            f.append(i)
            thru_sum.setdefault(sum, f)

        print(thru_sum)
        return res



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.subarraySum([1,2,3], 3)
print(r)
