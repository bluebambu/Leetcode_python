from collections import defaultdict, deque
from copy import deepcopy
from typing import List


# score:
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = defaultdict(lambda: False)
        q = deque()
        q.append(start)
        visited[str(start)] = True
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        def getNext(front, maze):
            x, y = front[0], front[1]
            n, m = len(maze), len(maze[0])
            r = []

            for d in dirs:
                x1, y1 = x+d[0], y+d[1]
                while x1>=0 and y1>=0 and x1<n and y1<m and maze[x1][y1] == 0:
                    x1, y1 = x1+d[0], y1+d[1]
                x1, y1 = x1-d[0], y1-d[1]
                if not (x1==x and y1==y):
                    r.append([x1, y1])

            return r


        while q:
            front = q.popleft()
            if front == destination:
                return True
            nexts = getNext(front, maze)
            print('front',front)
            print(nexts)
            for n in nexts:
                if not visited[str(n)]:
                    q.append(n)
                    visited[str(n)] = True

        return False



s = Solution()
m = [
[0,0,1,0,0],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0],
]
st = [0,4]
d = [4,4]
r = s.hasPath(m, st, d)
print(r)
assert r == True
