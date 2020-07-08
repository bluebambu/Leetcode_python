from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
