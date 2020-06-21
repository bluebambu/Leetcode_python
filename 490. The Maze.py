from collections import defaultdict, deque
from copy import deepcopy
from typing import List


# score:
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = defaultdict(lambda x: False)
        q = deque()
        q.append(start)
        visited[str(start)] = True

        def getNext(front, maze):
            x, y = front[0], front[1]
            n, m = len(maze), len(maze[0])
            r = []
            for y1 in range(y+1, m-1):
                if maze[x][y1] == 1:
                    r.append([x, y1])
                    break
            for y2 in range(y-1, 0, -1):
                if maze[x][y2] == 1:
                    r.append([x, y2])
                    break
            for x1 in range(x+1, n-1):
                if maze[x1][y] == 1:
                    r.append([x1, y])
                    break
            for x2 in range(x-1, 0, -1):
                if maze[x2][y] == 1:
                    r.append([x2, y])
                    break
            return r

        while q:
            front = q.popleft()
            if front == destination:
                return True
            nexts = getNext(front, maze)
            for n in nexts:
                if not visited[n]:
                    q.append(n)
                    visited[str(n)] = True

        return False



s = Solution()
r = s.hasPath([[1,0,1], [0,0,1]], [0,0], [1,1])
print(r)
assert r == True
