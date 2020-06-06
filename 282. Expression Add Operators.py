from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = 0
        for i, c in enumerate(num):
            pre, pos = num[:i+1], num[i+1:]
            if dfs(pos, target - int(pre)):
