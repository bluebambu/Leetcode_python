from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for j in range(n+1)] for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i==1 and j==1:
                    dp[1][1] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]

    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [ 1 for i in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]

        return dp[-1]

tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
