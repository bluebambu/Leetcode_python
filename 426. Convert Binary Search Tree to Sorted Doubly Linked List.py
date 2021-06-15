from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder, Node

# score: 26%
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def dfs(node: Node):
            if not node:
                return None, None
            lh, lt = dfs(node.left)
            rh, rt = dfs(node.right)
            head = lh if lh else node
            tail = rt if rt else node
            if lt:
                lt.right = node
                node.left = lt
            if rh:
                node.right = rh
                rh.left = node
            return head, tail

        first, last = dfs(root)
        last.right = first
        first.left = last
        return first


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
