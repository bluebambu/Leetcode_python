from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        if len(s) ==  1:
            return 0

        c=s[0]
        cnt=1
        cnt_arr = []

        for i in range(1, len(s)):
            if s[i] == c:
                cnt+=1
            else:
                c=s[i]
                cnt_arr.append(cnt)
                cnt = 1

        cnt_arr.append(cnt)

        res = 0
        if len(cnt_arr) == 1:
            return 0

        for i in range(0, len(cnt_arr)-1):
            res += min(cnt_arr[i], cnt_arr[i+1])

        return res



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
