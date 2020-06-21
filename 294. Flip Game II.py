from collections import defaultdict

# 80%
class Solution:
    def canWin(self, s: str) -> bool:
        m = defaultdict(bool)
        def win(s: str) -> bool:
            if s in m:
                return m[s]

            if len(s) < 2:
                return False

            for i in range(len(s) - 1):
                sub = s[i:i+2]
                if sub == "++" and not win(s[:i]+"--"+s[i+2:]):
                    m[s] = True
                    return True

            m[s] = False
            return False

        return win(s)

s = Solution()
r = s.canWin("++++")
print(r)
assert r == True
