from XiangUtils.xiangUtils import Tree


# score: 19%
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [-1 for _ in range(n)]
        res = []
        def conflict(board, i, v):
            # cur point: [i, v]
            for j in range(i):
                diff = i - j
                if abs(board[j] - v) == abs(diff):
                    return True
                if board[j] == v:
                    return True
            return False

        def tryQueen(i, board, res):
            if i == len(board):
                res.append([]+board)
                return
            for col in range(n):
                if not conflict(board, i, col):
                    board[i] = col
                    tryQueen(i+1, board, res)
                    board[i] = -1

        tryQueen(0, board, res)
        return len(res)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.totalNQueens(8)
print(r)
