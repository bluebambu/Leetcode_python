from collections import defaultdict
from typing import List

# score: 92%
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is subseq of t
        if s == '':
            return True

        n = len(t)
        j = 0
        for i in range(n):
            if t[i] != s[j]:
                continue
            else:
                j += 1
                if j == len(s):
                    break

        return j == len(s)

s = Solution()
r = s.isSubsequence("abc", "ahbgdc")
print(r)
assert r == True
r = s.isSubsequence("axc", "ahbgdc")
print(r)
assert r == False
