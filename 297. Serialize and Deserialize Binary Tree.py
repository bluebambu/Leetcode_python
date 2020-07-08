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


# score: 86.5%
class Codec:
    def serialize(self, root: TreeNode):
        if not root:
            return "#"
        return ','.join([str(root.val),
                         self.serialize(root.left),
                         self.serialize(root.right)])

    def deserialize(self, data: str):
        vals = data.split(',')
        i = 0

        def dfs(vals, i):
            if i >= len(vals) or vals[i] == '#':
                return None, i+1
            cur = TreeNode()
            cur.val = int(vals[i])
            i+=1
            cur.left, i = dfs(vals, i)
            cur.right, i = dfs(vals, i)
            return cur, i

        return dfs(vals, i)[0]


#tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
tree = Tree('1,2,3,#,#,4,5,#,#,#,#')
codec = Codec()
s = codec.serialize(tree.root)
print(s)
r = codec.deserialize(s)
lvlOrder(r)
