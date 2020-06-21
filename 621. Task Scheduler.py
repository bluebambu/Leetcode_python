from collections import defaultdict
from typing import List

class Solution2:
    def leastIntervalOutputString(self, tasks: List[str], n: int) -> str:
        m = defaultdict(int)
        for t in tasks:
            m[t] = m[t] + 1

        elem_cnt = [[k, v] for k, v in m.items()]
        elem_cnt = sorted(elem_cnt, key=lambda p: p[1], reverse=True)
        pos = [0 for _ in range(len(elem_cnt))]

        res = ""
        finished = 0

        while finished < len(elem_cnt):
            found = False
            for idx, pair in enumerate(elem_cnt):
                if pair[1] > 0 and pos[idx] <= len(res):
                    res += pair[0]
                    pos[idx] = len(res) + n # important
                    pair[1] = pair[1] - 1
                    if pair[1] == 0:
                        finished += 1
                    found = True
                    break # important
            if found == False:
                res += '^'

        return res


# 85.27%
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = defaultdict(int)
        for t in tasks:
            m[t] = m[t] + 1

        maxCnt = 0
        cntOfMax = 0
        for t in m:
            if m[t] > maxCnt:
                maxCnt = m[t]
                cntOfMax = 1
            elif m[t] == maxCnt:
                cntOfMax += 1

        needBlank = (maxCnt-1)*(n+1) + cntOfMax
        return max(needBlank, len(tasks))

n = 1
s = Solution()
t = ['a','a','b','c','d','f', 'a', 'a']
r = s.leastInterval(t, n)
print(r)
s2 = Solution2()
r2 = s2.leastIntervalOutputString(t, n)
print(r2)
print(len(r2))


