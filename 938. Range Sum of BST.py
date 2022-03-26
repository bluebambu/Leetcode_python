from collections import defaultdict
from queue import PriorityQueue
from typing import List, Optional
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(r: Optional[TreeNode], l, h):
            nonlocal res
            if r is None:
                return
            if l <= r.val <= h:
                res += r.val
                dfs(r.left, l, r.val-1)
                dfs(r.right, r.val+1, h)
            elif l > r.val:
                dfs(r.right, l, h)
            else:
                dfs(r.left, l, h)

        dfs(root, low, high)
        return res


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
