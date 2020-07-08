from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 99%
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []
        def dfs(left, right, path, r):
            if left==0 and right==0:
                r.append(''+path)
                return
            if left > 0:
                dfs(left-1, right, path+'(', r)
            if right > left:
                dfs(left, right-1, path+')', r)

        dfs(n-1, n, '(', r)
        return r


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.generateParenthesis(3)
print(r)
