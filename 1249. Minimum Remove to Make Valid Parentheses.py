from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s: str = process(s, '(')
        s: str = s[::-1]
        s: str = process(s, ')')
        return s[::-1]


def process(s: str, p: str) -> str:
    res = ''
    pCnt = 0
    for c in s:
        if c == p:
            pCnt += 1
            res += c
        elif c == (')' if p == '(' else '('):
            if pCnt > 0:
                pCnt -= 1
                res += c
        else:
            res += c

    return res


s = Solution()
r = s.minRemoveToMakeValid("ds(fjek)())")
print(r)
r = s.minRemoveToMakeValid("ds(fj(((ek)())")
print(r)
