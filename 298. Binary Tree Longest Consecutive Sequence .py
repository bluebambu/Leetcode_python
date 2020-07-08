from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score:  13%
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = 0
        def dfs(node: TreeNode, sz, parent: TreeNode):
            if not node:
                return
            cursz = 1
            if parent and parent.val + 1 == node.val:
                cursz = sz + 1
            nonlocal res
            res = max(res, cursz)
            dfs(node.left, cursz, node)
            dfs(node.right, cursz, node)

        dfs(root, 1, None)
        return res


tree = Tree('2,#,3,2,#,1,#,#,#')
s = Solution()
r = s.longestConsecutive(tree.root)
print(r)

tree = Tree('1,#,3,2,4,#,#,#,5,#,#')
s = Solution()
r = s.longestConsecutive(tree.root)
print(r)
