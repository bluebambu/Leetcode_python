from collections import deque, defaultdict
from typing import List
from queue import PriorityQueue


class TopoSort:
    def __init__(self, n, edges:List):
        # edges: [ [a, b], [.. ]]
        self.graph:dict[int, int] = self.gen(edges)  # dict of [ node, [nodes]]
        self.indegree:dict[int, int] = self.genIn(edges) # dict of [ node, num ]

    def genToposort(self):
        q = deque()
        for node, indg in self.indegree.items():
            if indg == 0:
                q.append(node)

        res = []
        while q:
            head = q.popleft()
            res.append(head)
            if head in self.graph:
                nxt = self.graph[head]
                self.indegree[nxt] -= 1
                if self.indegree[nxt] == 0:
                    q.append(nxt)

        return res

    def gen(self, edges:[]):
        g=defaultdict()
        for e in edges:
            frm, to = e[0], e[1]
            g[frm] = to
        return g

    def genIn(self, edges:[]):
        g=defaultdict(lambda:0)
        for e in edges:
            frm, to = e[0], e[1]
            g[frm]
            g[to] += 1
        return g

class ToposortDFS:  ## dfs 太麻烦了， 面试直接说不会
    pass



t = TopoSort(5, [[0,1], [2,1], [1,3], [4, 3]])
print(t.genToposort())

