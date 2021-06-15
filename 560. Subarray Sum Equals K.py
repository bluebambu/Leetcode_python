from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder, Node

# score:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        dp = [0]
        for n in nums:
            dp.append(n + dp[-1])

        thru_sum = {0: [-1]}

        i = 0
        for



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
