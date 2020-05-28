from typing import List


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
    s = Solution()
    assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert s.countComponents(3, [[1,0],[2,0]]) == 1
