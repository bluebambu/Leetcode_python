from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def calculate(self, s: str) -> int:
        # 234 + (23-948+03-(348+93-371)) - 457
        res, curNum, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isnumeric():
                curNum = curNum*10 + int(ss)
            elif ss in ['+', '-']:
                res += curNum * sign
                curNum = 0
                sign = 1 if ss == '+' else -1
            elif ss =='(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ss == ')':
                res += curNum*sign
                res *= stack.pop()
                res += stack.pop()
                curNum = 0
        return res + curNum*sign

    def calculate2(self, s: str) -> int:
        # 234 + (23-948+03-(348+93-371)) - 457
        return self.dfs(s, 0)[0]

    def dfs(self, s, idx):
        print(idx, s[idx])
        if idx >= len(s):
            return 0
        res, num, sign = 0, 0, 1
        while idx < len(s):
            if s[idx].isnumeric():
                num = num*10 + int(s[idx])
            elif s[idx] in ['+', '-']:
                res += sign * num
                num = 0
                sign = 1 if s[idx] == '+' else -1
            elif s[idx] == '(':
                num, idx = self.dfs(s, idx+1)
                res += sign * num
                num = 0
            elif s[idx] == ')':
                res += sign * num
                return res, idx
            idx +=1
        return res + sign*num, idx

    def calculate3(self, s: str) -> int:
        res, lastnum, stack, sign = 0, 0, [], 1
        s = s.replace(" ", "") + "+0"
        for c in s:
            if c.isnumeric():
                lastnum = 10*lastnum + int(c)
            elif c in "+-":
                res += sign * lastnum
                lastnum = 0
                sign = 1 if c=='+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * lastnum
                lastnum = 0
                sign = 1
                res *= stack.pop()
                res += stack.pop()
        return res




s = Solution()
r = s.calculate2("234 + (23-948+03-(348+93-371)) - 457")
print(r)
r = s.calculate("234 + (23-948+03-(348+93-371)) - 457")
print(r)
