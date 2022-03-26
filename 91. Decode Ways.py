from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score:
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 2:
            if int(s) > 0:
                return 1
            else:
                return 0

        dp = [0 for i in range(len(s))]

        dp[0] = (1 if dp[0]!='0' else 0)

        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if s[i-1] != '0' and 1<=int(s[i-1:i+1]) <= 26:
                dp[i] += (dp[i-2] if i>1 else 1)

        return dp[-1]


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.numDecodings2("226")
print(r)
