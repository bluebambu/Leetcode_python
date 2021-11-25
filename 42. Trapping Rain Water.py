from typing import List
from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        l_h = [height[0]]
        r_h = [height[-1]]

        for i, h in enumerate(height, 1):
            l_h.append(max(l_h[-1], h))
        for i, h in reversed(list(enumerate(height))):
            if i == 0:
                continue
            r_h.insert(0, max(r_h[0], h))

        ans = 0
        for i, h in enumerate(height,1):
            if i == l - 1:
                break
            ll_h = l_h[i-1]
            rr_h = r_h[i+1]
            ans += min(ll_h, rr_h) - h

        return ans


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
