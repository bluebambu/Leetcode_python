from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        search for next greater number.
        """
        i = len(nums) - 1

        while i> 0:
            # 1. search for a[i-1] < a[i], 忽略 a[i-1] ==  a[i]
            if nums[i-1] >= nums[i]:
                i -= 1
                continue

            # 2. search for the num on the right, just > nums[i-1]
            pivot = nums[i-1]
            j = len(nums) - 1
            while j > i-1:
                if nums[j] <= pivot:
                    j-=1
                    continue
                else:
                    break
            nums[i-1], nums[j] = nums[j], nums[i-1]

            # 3. reverse the right part
            nums[i:] = nums[i:][::-1]

            return

        nums.reverse()


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
l =[1,2,3,4]
s.nextPermutation(l)
print(l)
