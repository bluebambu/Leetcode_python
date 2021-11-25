import copy
from collections import defaultdict
from typing import List

# score: 
class Solution:
    def longestPalindromeSubseq2(self, s: str) -> int:
        l = len(s)
        #  dp[i][j] == i == j -> 1
        #              i+1 == j -> s[i]==s[j] ? 2 : 0
        #              i+1 < j  -> s[i]==s[j] ? 2+dp[i+1][j-1] : dp[i][j-1], dp[i+1][j]
        # i, j <-- i+1,j-1,   i, j-1,   i-1,j
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for j in range(l):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                elif i == j-1:
                    dp[i][j] = 2 if s[i]==s[j] else 1
                else:
                    if s[i]==s[j]:
                        dp[i][j] = max(2 + dp[i+1][j-1], dp[i][j-1], dp[i+1][j])
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return max(max(row) for row in dp)

    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [0 for _ in range(l)]
        for j in range(l):
            old_last = 0
            for i in range(j, -1, -1):
                old = dp[i]
                if i == j:
                    dp[i] = 1
                elif i + 1 == j:
                    dp[i] = 2 if s[i]==s[j] else 1
                else:
                    if s[i] == s[j]:
                        dp[i] = 2 + old_last
                    else:
                        dp[i] = max(dp[i+1], old)
                old_last = old

        return dp[0]



s = Solution()
r = s.longestPalindromeSubseq("bbbab")
print(r)
