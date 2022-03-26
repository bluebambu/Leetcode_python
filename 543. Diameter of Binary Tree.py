from collections import defaultdict
from queue import PriorityQueue
from typing import List, Optional
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        dfs(root, res)
        return res[0]

def dfs(root, res):
    if not root:
        return 0

    l_dep = dfs(root, res)
    r_dep = dfs(root, res)

    cur_dep = None
    if l_dep == 0 and r_dep == 0:
        cur_dep = 1
    else:
        cur_dep = 0



    return max(l)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
