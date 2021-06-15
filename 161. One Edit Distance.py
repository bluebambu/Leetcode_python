from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score:  15%
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if len(t) - len(s) > 1:
            return False

        i, j = 0, 0
        while i<len(s):
            if s[i] != t[j]:
                return s[i+1:] == t[j+1:] or s[i:] == t[j+1:]
            i+=1
            j+=1
        return len(s) == len(t) - 1




s = Solution()
r = s.isOneEditDistance('cab', 'ad')
print(r)
r = s.isOneEditDistance('a', '')
print(r)
