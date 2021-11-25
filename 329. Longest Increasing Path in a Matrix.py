from typing import List
from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])

        dp = [[-1 for i in range(m)] for j in range(n)]

        res = -1

        def dfs(i, j):
            if dp[i][j] > -1:
                return dp[i][j]

            dp[i][j] = 1

            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ii, jj = i+d[0], j+d[1]
                if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(ii, jj) + 1)

            return dp[i][j]

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                res = max(res, dfs(i, j))

        return res



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
res = s.longestIncreasingPath(matrix)
assert res == 4
