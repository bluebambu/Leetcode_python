from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
def genEdge(p1, p2):
    return [p2[0]-p1[0], p2[1]-p1[1]]


def calc(points, i, j, k):
    p1, p2, p3 = points[i], points[j], points[k]
    e1, e2 = genEdge(p1, p2), genEdge(p2, p3)
    return e1[0]*e2[1] - e1[1]*e2[0]


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        l = len(points)
        lastProd = None
        for i in range(l):
            j, k = (i+1)%l, (i+2)%l
            crossProd = calc(points, i, j, k)
            if crossProd == 0:
                continue
            if lastProd == None:
                lastProd = crossProd
                continue
            if crossProd * lastProd < 0:
                return False
            lastProd = crossProd

        return True






tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.isConvex([[0,0],[0,10],[10,10],[10,0],[5,5]])
print(r)
assert r == True
