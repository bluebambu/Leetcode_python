class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

# 77%
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        l, r = matrix[0][0], matrix[-1][-1] + 1
        while l+1 < r:
            mid = int((l+r)/2)
            if self.rank(mid, matrix) <= k:
                l = mid
            else:
                r = mid
        return l


    def rank(self, x, mtx):
        n, m = len(mtx), len(mtx[0])
        i, j = n-1, 0
        r = 0
        while i>=0 and i<n and j>=0 and j<m:
            if mtx[i][j] > x:
                i -= 1
            elif mtx[i][j] < x:
                r += i+1
                j += 1
            else:
                r += i
                j += 1

        return r + 1



matrix = [
             [1, 5, 9],
             [10, 11, 13],
             [12, 13, 15]
         ]
k = 8
s = Solution()
r = s.kthSmallest(matrix, k)
print(r)




