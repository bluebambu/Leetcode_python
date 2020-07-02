from collections import deque
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lvlOrder(node: TreeNode) -> str:
    q = deque()
    q.append(node)
    r = []
    while q:
        f = q.popleft()
        r.append('#' if not f else str(f.val))
        if f:
            q.append(f.left)
            q.append(f.right)
    return ','.join(r)



class Tree:
    def __init__(self):
        self.root = TreeNode()

    def __init__(self, s: str):
        self.root = self.deserialize(s)

    def deserialize(self, s: str):
        nodes = s.split(',')
        i = 0
        root = TreeNode(val=nodes[i])
        i += 1
        q = deque()
        q.append(root)
        while q and i<len(s):
            f = q.popleft()
            if nodes[i] != '#':
                f.left = TreeNode(nodes[i])
                q.append(f.left)
            i += 1
            if nodes[i] != '#':
                f.right = TreeNode(nodes[i])
                q.append(f.right)
            i += 1

        return root

#
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        r = set()
        cache = {}

        def postOrder(node: TreeNode, r):
            if not node:
                return '#'

            serialize = str(node.val)+','+\
                        postOrder(node.left, r)+','+\
                        postOrder(node.right, r)
            if serialize not in cache:
                cache[serialize] = node
            else:
                r.add(cache[serialize])
            return serialize

        postOrder(root, r)
        return r


s = Solution()
tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
r = s.findDuplicateSubtrees(tree.root)
for e in r:
    print(lvlOrder(e))



