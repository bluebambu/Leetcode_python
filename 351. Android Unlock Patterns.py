from collections import defaultdict
from typing import List, Set


# score: 31%
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def getBtw(a, b):
            if a > b:
                a, b = b, a
            table = {
                (1, 3): 2,
                (1, 7): 4,
                (1, 9): 5,
                (2, 8): 5,
                (3, 7): 5,
                (3, 9): 6,
                (4, 6): 5,
                (7, 9): 8,
            }
            return table.get((a, b), None)

        def valid(i, l, v):
            if i in v:
                return False
            last = l[-1]
            mid = getBtw(i, last)
            if mid != None and mid not in v:
                return False
            else:
                return True

        def dfs(l, v, m, n):
            r = 0
            if len(l) >= m and len(l) <= n:
                r = 1
            if len(l) > n:
                return 0

            for i in range(1, 10):
                if valid(i, l, v):
                    print(i, l)
                    v.add(i)
                    l.append(i)
                    r += dfs(l, v, m, n)
                    v.remove(i)
                    l.pop()

            return r


        def calc(start, m, n):
            l = [start]
            v = set()
            v.add(start)
            return dfs(l, v, m, n)

        r1 = calc(1, m, n)
        r2 = calc(2, m, n)
        r3 = calc(5, m, n)
        print(r1, r2, r3)
        return 4*r1 + 4*r2 + r3


s = Solution()
r = s.numberOfPatterns(3, 7)
print(r)
