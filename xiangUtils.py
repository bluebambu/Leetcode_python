from collections import deque

DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lvlOrder(node: TreeNode) -> None:
    q = deque()
    q.append(node)
    r = []
    while q:
        sz = len(q)
        cur = []
        for _ in range(sz):
            f = q.popleft()
            cur.append('#' if not f else f.val)
            if f:
                q.append(f.left)
                q.append(f.right)
        r.append([] + cur)

    for l in r:
        print(l)


class Tree:
    def __init__(self):
        self.root = TreeNode()

    def __init__(self, s: str):
        self.root = self.deserialize(s)

    def deserialize(self, s: str) -> TreeNode:
        nodes = s.split(',')
        i = 0
        root = TreeNode(val=int(nodes[i]))
        i += 1
        q = deque()
        q.append(root)
        while q and i < len(s):
            f = q.popleft()
            if nodes[i] != '#':
                f.left = TreeNode(int(nodes[i]))
                q.append(f.left)
            i += 1
            if nodes[i] != '#':
                f.right = TreeNode(int(nodes[i]))
                q.append(f.right)
            i += 1

        return root


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
