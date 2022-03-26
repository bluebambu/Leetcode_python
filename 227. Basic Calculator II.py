from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
def do(mdRes, lastNum, mdSign):
    if mdSign == '*':
        mdRes *= lastNum
    elif mdSign == '/':
        mdRes = int(mdRes / lastNum)
    return mdRes


class Solution:
    # 2 + 4*3/4 - 3
    # 2 4 3 4
    # + * /
    def calculate(self, s: str) -> int:
        s = s + ' + 0'
        res, lastNum, pmSign = 0,0,1
        mdRes, mdSign, isMD = 1, '*', False
        for c in s:
            if c.isnumeric():
                lastNum = lastNum*10 + int(c)
            elif c in '*/':
                isMD = True
                mdRes = do(mdRes, lastNum, mdSign)
                mdSign = c
                lastNum = 0
            elif c in '+-':
                if isMD:
                    isMD = False
                    mdRes = do(mdRes, lastNum, mdSign)
                    res += pmSign * mdRes
                    mdRes = 1
                    mdSign = '*'
                else:
                    res += pmSign * lastNum
                pmSign = 1 if c == '+' else -1
                lastNum = 0
            # print(c, res, lastNum, mdRes, pmSign)

        return res


s = Solution()
r = s.calculate("1 + 4/4 - 4*4/4 - 3")
print(r)
