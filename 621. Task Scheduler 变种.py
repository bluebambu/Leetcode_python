from collections import defaultdict
from typing import List

class Solution:
    def leastInterval(self, tasks, n: int) -> str:
        """
        AABACCBAA, gap = 2 --> A--AB-AC--CBA--A  , LEN = 16
        """
        r = 0
        pos = defaultdict(int)
        for t in tasks:
            print(t, pos[t])
            while r < pos[t]:
                r+=1
            r+=1
            pos[t] = r+n
        return r


s = Solution()
t = "AABACCBAA"
# AABACCBAA, gap = 2 --> A--AB-AC--CBA--A, LEN = 16
r = s.leastInterval(t, 2)
print(r)
assert r == 16

t2 = ['a', 'a', 'b', 'a', 'b', 'b', 'a', 'a']
# a*abab*ba*a == 11
r = s.leastInterval(t2, 1)
print(r)
assert r == 11

