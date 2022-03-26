from collections import defaultdict
from functools import reduce
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    # 2 + 4*3/4 - 3
    def calculate(self, s: str) -> int:
        stack = []
        lastNum, sign = 0, 1
        mdSign = '*'
        i=0
        s = '+' + s.replace(" ", "")
        while i < len(s):
            c = s[i]
            if c in '+-':
                j = i+1
                while j<len(s) and s[j].isnumeric():
                    j+=1
                nextNum = int(s[i+1:j])
                i = j
                sign = 1 if c=='+' else -1
                stack.append(sign * nextNum)
            elif c in '*/':
                j = i+1
                while j<len(s) and s[j].isnumeric():
                    j+=1
                nextNum = int(s[i+1:j])
                i = j

                if c=='*':
                    stack.append(nextNum * stack.pop())
                else:
                    stack.append(int(stack.pop()/nextNum))
            else:
                i += 1

        return reduce(lambda a,b: a+b, stack)

    # 2 + 4*3/4 - 3
    def calculate2(self, s: str) -> int:
        prev_num = 0
        prev_sign = '+'
        stack = []
        res = 0

        for c in s:
            if c.isnumeric():
                prev_num = 10*prev_num + int(c)
            elif c in '+-':
                res += prev_num * (1 if prev_sign == '+' else -1)
                prev_sign = c
                prev_num = 0
            elif c in '*/':
                if prev_sign in '+-':
                    stack.append(res)
                    stack.append(prev_sign)
                    prev_sign = c





s = Solution()
r = s.calculate("1 + 4/4 - 4*4/4 - 3")
# r = s.calculate(" 3/2 ")
print(r)
