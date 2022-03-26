from collections import defaultdict
from queue import PriorityQueue
from typing import List, Optional
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dfs(root, res)
        return res

def dfs(root, res:list) -> int:
    if root == None:
        return 0

    left_dep = dfs(root.left, res)
    right_dep = dfs(root.right, res)

    cur_dep = max(left_dep, right_dep) + 1

    if len(res) < cur_dep:
        res.append([])

    res[cur_dep-1].append(root.val)

    return cur_dep


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
lvlOrder(tree.root)

s = Solution()
r = s.findLeaves(tree.root)
print(r)
