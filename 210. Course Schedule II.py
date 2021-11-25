from collections import defaultdict
from typing import List
from XiangUtils.xiangUtils import Tree


# score:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq: [[0,1] , [2,3] , [..] ]
        map = defaultdict(lambda:[])
        inorder = defaultdict(lambda:0)
        for pair in prerequisites:
            f, t = pair[1], pair[0]
            inorder[f]
            map[f].append(t)
            inorder[t] += 1

        res=[]
        for k in inorder:
            v = inorder[k]
            if v == 0:
                res.append(v)

        while res:
            front = res[0]





tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
