from collections import defaultdict


# 98.23%
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        g = defaultdict(lambda: 0)
        for c in t:
            g[c] = g[c] + 1
        cnt = len(g)

        i, j = 0, 0 # [ ) range
        res = len(s) + 1 # make sure to be bigger than len(s)
        r = []
        while True:
            while j < len(s) and cnt > 0:
                c = s[j]
                g[c] = g[c] - 1
                if g[c] == 0:
                    cnt -= 1
                j += 1

            while i < j and cnt == 0:
                c = s[i]
                g[c] = g[c] + 1
                if g[c] > 0:
                    cnt += 1
                i += 1

            if res > j-i+1:
                res = j-i+1
                r = [i-1, j]

            if j == len(s):
                break

        if r == []:
            return  ""
        return s[r[0]:r[1]]

if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("AAABBT", "ABBT") == "ABBT"
    assert s.minWindow("A", "A") == "A"

