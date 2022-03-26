from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        keypad = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
        ]

        res = []
        if digits == "":
            return []

        for c in digits:
            n = int(c)
            chars = keypad[n]
            if not res:
                res = chars
            else:
                nextRes = []
                for char in chars:
                    for rec in res:
                        nextRes.append(rec + char)
                res = nextRes

        return res


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.letterCombinations("23")
print(r)
