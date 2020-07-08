from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 55%
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        r = 0
        def calc(nums, biggestId):
            if biggestId < 2:
                return 0
            i, j = 0, biggestId - 1
            r = 0
            while i<j:
                if nums[i] + nums[j] <= nums[biggestId]:
                    i += 1
                else:
                    r += j-i
                    j -= 1
            return r


        for idx in range(len(nums)-1, 0, -1):
            possible = calc(nums, idx)
            r += possible
        return r


s = Solution()
r = s.triangleNumber([2,2,3])
print(r)
r = s.triangleNumber([2,2,3,4])
print(r)
r = s.triangleNumber([2,2,2,3])
print(r)
