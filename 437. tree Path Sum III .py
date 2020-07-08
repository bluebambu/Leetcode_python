from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 41%
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        r = []
        presum_map = defaultdict(list)
        presum_map[0] = [None]

        def dfs(node, k, r, presum):
            if not node:
                return
            cv = int(node.val) + presum
            tgt = cv - k
            if tgt in presum_map:
                start_points = presum_map[tgt]
                for p in start_points:
                    r.append([p, node])
            presum_map[cv].append(node)
            dfs(node.left, k, r, cv)
            dfs(node.right, k, r, cv)
            presum_map[cv].pop()

        dfs(root, sum, r, 0)
        return r


tree = Tree('10,5,-3,3,2,#,11,3,-2,#,1,#,#,#,#,#,#,#,#')
s = Solution()
r = s.pathSum(tree.root, 8)
print(len(r))
for l in r:
    print(l[0].val, l[1].val)
