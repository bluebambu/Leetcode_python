from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
def initLeft(leftProd, nums):
    cum = 1
    for v in nums:
        cum *= v
        leftProd.append(cum)


def initRight(rightProd, nums):
    cum = 1
    for v in reversed(nums):
        cum *= v
        rightProd.append(cum)
    rightProd.reverse()


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftProd, rightProd = [], []

        initLeft(leftProd, nums)
        initRight(rightProd, nums)

        res = []
        for i, v in enumerate(nums):
            if i == 0:
                res.append(rightProd[1])
            elif i == n-1:
                res.append(leftProd[-2])
            else:
                res.append(leftProd[i-1]*rightProd[i+1])

        return res


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.productExceptSelf([1,2,3,4])
r = s.productExceptSelf([1,1,1,0,-2,-4])
print(r)
