from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        r = []
        postOrder(root, r)
        return r


s = Solution()
r = s.kthSmallest(matrix, k)
print(r)
assert r == 1
