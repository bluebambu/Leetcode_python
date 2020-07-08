from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def sym(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and sym(p.left, q.right) and sym(p.right, q.left)

        return sym(root.left, root.right)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
