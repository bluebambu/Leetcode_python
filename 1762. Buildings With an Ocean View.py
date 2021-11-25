from typing import List
from XiangUtils.xiangUtils import Tree


# score: 99%
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        highest = -1
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > highest:
                res.append(0, i)
                highest = heights[i]

        return reversed(res)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.findBuildings([4,2,3,1])
assert r == [0,2,3]
r = s.findBuildings([4,3,2,1])
assert r == [0,1,2,3]
r = s.findBuildings([1,3,2,4])
assert r == [3]
