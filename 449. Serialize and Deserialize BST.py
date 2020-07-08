from collections import defaultdict
from typing import List
from collections import deque


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

    s = ','.join(r)
    print(s)
    return s


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
        while q and i < len(s):
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


# score:
class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        res = str(root.val)
        left = self.serialize(root.left)
        if left:
            res += ','+left
        right = self.serialize(root.right)
        if right:
            res += ','+right
        return res

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        vals = data.split(',')

        def dfs(vals, i, j):
            if i >= len(vals) or i >= j:
                return None

            cur = TreeNode()
            cur.val = int(vals[i])
            k = i+1
            while k<j:
                if int(vals[k]) > int(vals[i]):
                    break
                k += 1
            cur.left = dfs(vals, i+1, k)
            cur.right = dfs(vals, k, j)
            return cur

        return dfs(vals, 0, len(vals))


tree = Tree('5,3,7,1,4,6,8,#,#,#,#,#,#,#,#')
tree2 = Tree('2,1,3,#,#,#,#')
s = Codec()
r = s.serialize(tree2.root)
print(r)
lvlOrder(s.deserialize(r))
