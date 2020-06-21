from collections import defaultdict
from typing import List

# score:
class Solution(object):
    def dungeonGame(self, map):
        """
        dp[i][j] <-- dp[i+1][j], dp[i][j+1]

        for (i+1, j): if dp[i+1][j] <= map[i+1][j], cand1 = 1
                      else: cand1 = dp[i+1][j] - map[i+1][j]

        dp[i][j] = min( cand1, cand2 )
        """


s = Solution()
r = s.canWin()
print(r)
assert r == True
