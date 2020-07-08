from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score:
class Solution:
    def LCAofDeepest(self, root: TreeNode):
        def dfs(node):
            if not node:
                return node, 0
            if not node.left and not node.right:
                return node, 1
            ln, ld = dfs(node.left)
            rn, rd = dfs(node.right)
            if ld > rd:
                return ln, ld+1
            elif ld < rd:
                return rn, rd+1
            else:
                return node, ld+1

        return dfs(root)[0]


tree = Tree('1,2,3,4,5,6,7,8,#,#,#,#,#,#,9,#,#,#,#')
s = Solution()
r = s.LCAofDeepest(tree.root)
print(r.val)
