from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # dp[i] = dp[i-1] + (i-last_char_i) - (last_char_i - last_2nd_char_i)
        last_2nd_idx, last_idx = [-1 for i in range(26)], [-1 for i in range(26)]

        dp = [0 for i in range(len(s))]

        dp[0] = 1
        last_idx[getDist(s[0])] = 0

        for i in range(1, len(s)):
            c = s[i]
            distToLast = i - last_idx[getDist(c)]
            distToLast2nd = (last_idx[getDist(c)] - last_2nd_idx[getDist(c)])
            dp[i] = dp[i-1] + distToLast - distToLast2nd

            last_2nd_idx[getDist(c)] = last_idx[getDist(c)]
            last_idx[getDist(c)] = i

        return sum(dp)

def getDist(char):
    return ord(char) - ord('a')


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.uniqueLetterString("aba")
print(r)
r = s.uniqueLetterString("abc")
print(r)

