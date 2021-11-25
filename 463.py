from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def getPerimeter(self, islands: List[List]):
        perimeter = 0
        visited = set()

        for x in range(len(islands)):
            for y in range(len(islands[x])):
                if (x, y) not in visited:
                    self.bfs(islands, x, y, visited, perimeter)

        return perimeter

    def bfs(self, islands, x, y, visited, perimeter):
        q=deque()
        q.append([x, y])
        visited.add((x, y))

        while q:
            head:List = q.popleft()
            for d in dirs:
                x1, y1 = x+d[0], y+d[1]
                if x1>=0 and y1>=0 and x1<m and y1<n and islands[x1][y1] and tuple(x1, y1) not in visited:
                    visited.add((x1, y1))
                    q.append([x1, y1])

        return perimeter



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()

s=set()
s.add(tuple([1,1]))
print(s)
