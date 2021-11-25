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


class listNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = listNode(None)
        self.end = listNode(None)
        self.head.next = self.end
        self.end.prev = self.head

        self.size = 0

    def append(self, val) -> listNode:
        newNode = listNode(val)
        newNode.next = self.end
        newNode.prev = self.end.prev
        self.end.prev.next = newNode
        self.end.prev = newNode
        self.size += 1
        return newNode

    def appendLeft(self, val) -> listNode:
        newNode = listNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1
        return newNode

    def get(self, val) -> listNode:
        n: listNode = self.head.next
        while n is not self.end:
            if n.val == val:
                return n
            n = n.next
        return None

    def removeNode(self, tgt: listNode) -> bool:
        n: listNode = self.head.next
        while n is not self.end:
            if n is tgt:
                p, n2 = n.prev, n.next
                p.next = n2
                n2.prev = p
                self.size -= 1
                return n
            n = n.next

        return None

    def removeOneValue(self, val) -> bool:
        n: listNode = self.head.next
        while n is not self.end:
            if n.val == val:
                p, n = n.prev, n.next
                p.next = n
                n.prev = p
                self.size -= 1
                return True
            n = n.next

        return False

    def size(self) -> int:
        return self.size

    def pop(self) -> listNode:
        self.checkNotEmpty()
        tail = self.end.prev
        return self.removeNode(tail)

    def popLeft(self) -> listNode:
        self.checkNotEmpty()
        head = self.head.next
        return self.removeNode(head)

    def tailNode(self):
        self.checkNotEmpty()
        return self.end.prev

    def headNode(self):
        self.checkNotEmpty()
        return self.head.next

    def checkNotEmpty(self):
        if self.size == 0:
            return None
