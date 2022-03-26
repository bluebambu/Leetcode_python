from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = []

        cum = 1
        for v in nums:
            cum *= v
            leftProd.append(cum)

        i = len(leftProd)-1
        cumRight = 1
        while i>=0:
            if i == len(leftProd) - 1:
                leftProd[i] = leftProd[i-1]
                cumRight *= nums[i]
            elif i == 0:
                leftProd[i] = cumRight
            else:
                leftProd[i] = leftProd[i-1] * cumRight
                cumRight *= nums[i]

            i -= 1

        return leftProd



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.productExceptSelf([1,2,3,4])
print(r)
r = s.productExceptSelf([1,1,1,0,-2,-4])
print(r)
