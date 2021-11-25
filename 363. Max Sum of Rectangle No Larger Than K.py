import bisect
from typing import List
from XiangUtils.xiangUtils import Tree


# score:  did not pass the last big dataset.
class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        LOWEST = -10000000000000000000000000000000000
        res = LOWEST
        cumMtx = [[0 for _ in range(m)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                cumMtx[i+1][j] = cumMtx[i][j] + matrix[i][j]

        print(cumMtx)

        def cumsum(i, j, k):
            return cumMtx[i+1][k] - cumMtx[j][k]

        def getRangeSumNoLargerK(i, j, k):
            cum = [0]
            r2 = LOWEST
            for ii in range(0, m):
                cur = cumsum(i, j, ii) + cum[-1]
                tgt = cur - k
                cands = list(filter(lambda x: x>=tgt, cum))
                if len(cands):
                    cand = min(cands)
                    r2 = max(r2, cur - cand)
                cum += [cur]

            return r2 if r2 != LOWEST else None

        for i in range(n):
            for j in range(i+1):
                # rows in [j, i]
                cur = getRangeSumNoLargerK(i, j, k)
                if cur != None and cur > res:
                    res = cur

        return res if res != LOWEST else None



# score: 5%
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        LOWEST = float('-inf')
        res = LOWEST

        def noLargerThanK(colSum, k):
            # dim of colSum: m+1
            recSum = [0]
            prefix_sum = 0
            r2 = float('-inf')
            for s in colSum:
                prefix_sum += s
                tgt = prefix_sum - k
                # look for pos that >= tgt
                insert_pos = bisect.bisect_left(recSum, tgt)
                if insert_pos == len(recSum):
                    # no candidates
                    pass
                else:
                    cand = prefix_sum - recSum[insert_pos]
                    r2 = max(r2, cand)

                bisect.insort(recSum, prefix_sum)

            return r2

        for i in range(n):
            colSum = [0 for _ in range(m)]
            for j in range(i, n):
                # [i, j]
                for jj in range(m):
                    colSum[jj] += matrix[j][jj]
                cur = noLargerThanK(colSum, k)
                if cur!=float('-inf') and cur > res:
                    res = cur
        return res



matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
s = Solution()
k = 0
assert s.maxSumSubmatrix(matrix, k) == 0

tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
matrix = [
    [1,0,1],
    [0,-2,3]
]
k = 2
s = Solution()
r = s.maxSumSubmatrix(matrix, k)
print(r)
assert r == 2

matrix = []
s = Solution()
k = 1
assert s.maxSumSubmatrix(matrix, k) == 0

matrix = [[2,2,-1]]
s = Solution()
k = 0
print(s.maxSumSubmatrix(matrix, k))
assert s.maxSumSubmatrix(matrix, k) == -1


