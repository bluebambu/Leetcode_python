import heapq
from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

    def __repr__(self):
        return str([self.start, self.end])


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> '[Interval]':
        pq = []
        for employee in schedule:
            pq.append((employee[0], 0, employee))

        heapq.heapify(pq)

        pivot_intvl, _, pivot_emply = heapq.heappop(pq)

        res = []

        if len(pivot_emply) > 1:
            heapq.heappush(pq, (pivot_emply[1], 1, pivot_emply))

        while pq:
            top_intvl, top_idx, top_emply = heapq.heappop(pq)

            if top_idx < len(top_emply) - 1:
                heapq.heappush(pq, (top_emply[top_idx+1], top_idx+1, top_emply))

            if top_intvl.start > pivot_intvl.end:
                res.append((pivot_intvl.end, top_intvl.start))
                pivot_intvl = top_intvl
            else:
                pivot_intvl = Interval(pivot_intvl.start, max(pivot_intvl.end, top_intvl.end))

        return res


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.employeeFreeTime([[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]])
print(r)


r = s.employeeFreeTime([[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]])
print(r)
