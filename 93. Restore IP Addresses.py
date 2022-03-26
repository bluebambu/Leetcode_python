from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        dfs(s, 4, path, res)
        return res

def dfs(s:str, seg:int, path, res):
    if not s and seg > 0:
        return
    if not s and seg == 0:
        res.append('.'.join(path))
        return
    if s and seg==0:
        return

    for i, c in enumerate(s):
        head = s[:i+1]
        if isValid(head):
            path.append(head)
            dfs(s[i+1:], seg-1, path, res)
            path.pop()
        else:
            break

def isValid(n:str):
    if len(n)>1 and n[0]=='0':
        return False
    if int(n) > 255:
        return False
    return True




tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.restoreIpAddresses("25525511135")
print(r)
