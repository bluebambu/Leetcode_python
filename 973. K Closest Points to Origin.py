from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node
import heapq


# score: 9%
def getRank(points, left, right):
    pivot = points[left]
    i, j = left+1, right

    while i<j:
        while i<j and (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
            i+=1
        while i<j and (points[j-1][0]**2 + points[j-1][1]**2) >= (pivot[0]**2 + pivot[1]**2):
            j -= 1

        if i==j:
            break

        points[i], points[j-1] = points[j-1], points[i]

    points[left], points[i-1] = points[i-1], points[left]

    return i-1


def quickSelect(points, k):
    left, right = 0, len(points)

    while left < right -1:
        rank = getRank(points, left, right)
        if rank == k-1:
            break
        elif rank < k-1:
            left = rank + 1
        else:
            right = rank

    return points[:k]


class Solution:
    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        # best is to use quick select
        return quickSelect(points, k)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        class Node:
            def __init__(self, p):
                self.val = p

            def __lt__(self, other):
                return self.getDist(self.val) > self.getDist(other.val)

            def getDist(self, p):
                return p[0]**2 + p[1]**2

            def __str__(self):
                return self.val

        for p in points:
            l = len(maxheap)
            if l < k:
                heapq.heappush(maxheap, Node(p))
            else:
                heapq.heappushpop(maxheap, Node(p))

        return [i.val for i in maxheap]




tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
# r = s.kClosest([[1,3],[-2,2]], 1)
# print(r)
r = s.kClosest([[3,3],[5,-1],[-2,4]],2)
print(r)
# r = s.kClosest([[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[1,1]],1)
# print(r)
# r = s.kClosest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]], 5)
# print(r)
# r = s.kClosest([[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]], 5)
# print(r)
