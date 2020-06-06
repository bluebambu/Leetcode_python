from typing import List

# 89%
class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        cur_sum = sum(nums)
        left = 0
        right = cur_sum

        def lessSegmentOrEq(nums, localSum, m):
            cnt = 0
            s = localSum
            for i in nums:
                if s < i:
                    cnt += 1
                    s = localSum
                    if localSum < i:
                        return False
                s = s - i
            return cnt+1 <= m

        while left+1<right:
            mid = int((left+right)/2)
            if lessSegmentOrEq(nums, mid, m):
                right = mid
            else:
                left = mid
        return right

# 11.21%
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        # dp = (n+1)*[(m+1)*[0]]  # this expr is toxic!
        dp = [[0 for y in range(m+1)] for x in range(n+1)]
        cum = (n+1) * [0]
        for i in range(1, n+1):
            cum[i] = cum[i-1] + nums[i-1]
        print(cum)

        def rangeSum(i, j): # [ ]
            return cum[j+1] - cum[i]

        for j in range(1, n+1):
            dp[j][1] = cum[j]
        print(dp[0][1] is dp[1][1])
        print(dp)

        for j in range(2, m+1):
            for i in range(0, n+1):
                if i < j:
                    dp[i][j] = 0
                else:
                    cur_min = sum(nums)
                    for k in range(j-1, i+1):
                        # last segment: [k, i-1]
                        lastSum = rangeSum(k, i-1)
                        prevMinMax = dp[k][j-1]
                        cur_min = min(cur_min, max(lastSum, prevMinMax))
                    dp[i][j] = cur_min

        return dp[n][m]



s = Solution2()
r = s.splitArray([1,2,5,3,2], 3)
print(r)

