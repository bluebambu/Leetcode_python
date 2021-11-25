from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                dp[i][j] = True if i==j else (True if s[i]==s[j] and (i==j-1 or dp[i+1][j-1]) else False)

        for r in dp:
            print(r)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.longestPalindrome("abbac")
print(r)
