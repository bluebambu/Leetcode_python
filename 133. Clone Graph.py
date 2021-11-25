from collections import deque
from XiangUtils.xiangUtils import Tree


# score:
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# 7%
# bfs: 20%
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cache = {}
        def dfs(node: Node):
            if not node:
                return None
            if node in cache:
                return cache[node]
            cur = Node(node.val)
            cache[node] = cur
            for c in node.neighbors:
                cur.neighbors.append(dfs(c))
            return cur

        def bfs(node: Node):
            if not node:
                return None
            q = deque()
            cache = {}
            cache[node] = Node(node.val)
            q.append(node)
            while q:
                f = q.popleft()
                for c in f.neighbors:
                    if c not in cache:
                        cache[c] = Node(c.val)
                        q.append(c)
                    cache[f].neighbors.append(cache[c])
            return cache[node]


        return bfs(node)



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
