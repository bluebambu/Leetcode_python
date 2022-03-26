from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        n, m = len(grid), len(grid[0])
        q = deque()
        visited = set()

        state = (0,0,k)
        visited.add(state)
        q.append((0, state))

        while q:
            steps, old_state = q.popleft()
            x, y, remains = old_state

            if x==n-1 and y==m-1:
                return steps

            for xx, yy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if xx<0 or xx>=n or yy<0 or yy>=m:
                    continue
                new_remains = remains - grid[xx][yy]
                new_state = (xx, yy, new_remains)

                if new_state not in visited and new_remains >= 0:
                    visited.add(new_state)
                    q.append((steps+1, new_state))


        return -1





tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
print(r)


r = s.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1)
print(r)
