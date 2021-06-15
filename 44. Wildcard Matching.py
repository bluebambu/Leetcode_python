from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        dp[i][j] =
            p[j] != '?''*'
                s[i] == p[j] and dp[i-1][j-1]
            p[j] == '?'
                dp[i-1][j-1]
            p[j] == '*'
                dp[i-1][j-1] or dp[i-1][j]
        '''


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
