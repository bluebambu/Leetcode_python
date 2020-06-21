from collections import defaultdict
from typing import List


# 75%
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        init = 0
        s = defaultdict(bool)

        def win(state, size, target):
            if state in s:
                return s[state]
            if target <= 0:
                return False

            for i in range(size):
                if not (state & (1<<i)):
                    next = (state | (1<<i))
                    if not win(next, size, target - (i+1)):
                        s[state] = True
                        return True

            s[state] = False
            return False

        return win(init, maxChoosableInteger, desiredTotal)


s = Solution()
r = s.canIWin(4, 6)
print(r)
assert r == True
