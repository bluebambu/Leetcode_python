from collections import deque
from typing import List


class Solution4:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(x, v, g):
            q = deque()
            q.append(x)
            v[x] = 1
            while len(q):
                f = q.popleft()
                for nxt in g[f]:
                    if v[nxt] == 0:
                        v[nxt] = 2
                        q.append(nxt)


        g = {x:set() for x in range(n)}
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])

        res = 0
        v = [0]*n
        for x in range(n):
            if v[x] == 0:
                bfs(x, v, g)
                res += 1

        return res



# 90.75%
class Solution3:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(x, g, v):
            v[x] = 1
            for next in g[x]:
                if v[next] == 0:
                    dfs(next, g, v)

        g = {x: set() for x in range(n)}
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])

        res = 0
        v = [0]*n
        for x in range(n):
            if v[x] == 0:
                dfs(x, g, v)
                res += 1

        return res


# better solution
class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        def unify(xy):
            x, y = map(find, xy)
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = parent[x]
                if rank[x] == rank[y]:
                    rank[x] += 1

        parent, rank = range(n), [0]*n
        map(unify, edges)
        return len({find(x) for x in parent})


# 6.59%
class Solution:
    def __init__(self):
        self.roots = None

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.roots = [-1] * n
        for e in edges:
            self.combine(e[0], e[1])

        return self.roots.count(-1)

    def combine(self, i, j):
        ri, rj = self.root(i, self.roots), self.root(j, self.roots)
        if ri == rj:
            return
        self.roots[rj] = ri

    def root(self, i, roots):
        if (roots[i] == -1):
            return i
        return self.root(roots[i], roots)

if __name__ == "__main__":
    s = Solution4()
    assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert s.countComponents(3, [[1,0],[2,0]]) == 1
