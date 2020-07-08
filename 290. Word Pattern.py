from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 16%
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words: List = str.split(' ')
        p2w = defaultdict(lambda: str)
        w2p = defaultdict(lambda: str)
        i = 0
        while i < len(words):
            if i >= len(pattern):
                return False
            p, w = pattern[i], words[i]
            if p not in p2w and w not in w2p:
                p2w[p] = w
                w2p[w] = p
            elif p2w[p] != w or w2p[w] != p:
                return False
            i += 1

        return i == len(pattern)





tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
