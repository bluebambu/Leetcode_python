from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score:
class SparseVector:
    def __init__(self, nums: List[int]):
        self.h = {}
        for i in range(len(nums)):
            v = nums[i]
            if v != 0:
                self.h[i] = v

    def getHashmap(self):
        return self.h

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        h2 = vec.getHashmap()
        res = 0
        for k, v in self.h.items():
            if k in h2:
                res += self.h[k] * h2[k]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
