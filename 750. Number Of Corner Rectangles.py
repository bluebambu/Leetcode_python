from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 93.92%
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        cache = []
        for r in grid:
            cache.append(set())
            for i, c in enumerate(r):
                if c == 1:
                    cache[-1].add(i)

        r = 0
        i = 0
        for i in range(len(cache)):
            s1 = cache[i]
            for j in range(i+1, len(cache)):
                s2 = cache[j]
                NCommon = len(s1.intersection(s2))
                if NCommon > 1:
                    r += NCommon*(NCommon-1)/2

        return int(r)


s = Solution()
r = s.kthSmallest(matrix, k)
print(r)
assert r == 1
