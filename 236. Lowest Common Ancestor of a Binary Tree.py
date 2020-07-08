from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 20%
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        r1 = self.lowestCommonAncestor(root.left, p, q)
        r2 = self.lowestCommonAncestor(root.right, p, q)
        if root == p or root == q or (r1 and r2):
            return root
        elif r1 or r2:
            return r1 if r1 else r2
        else:
            return None


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
