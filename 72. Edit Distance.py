from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = min(dp[i - 1][j - 1] + 1
                               ,dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1)

        return dp[-1][-1]


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.minDistance('ab', 'abc')
print(r)
r = s.minDistance('a', 'ac')
print(r)
r = s.minDistance('horse', 'ros')
print(r)
