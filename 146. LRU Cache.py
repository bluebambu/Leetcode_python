from XiangUtils.xiangUtils import Tree


# score:
class node:
    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = node(0)
        self.tail = node(0)
        self.cap = capacity
        self.sz = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        v = self.map.get(key).val
        self.moveToTop(self.map.get(key))
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            n = self.map.get(key)
            n.val = value
            self.moveToTop(n)
        else:
            if self.sz == self.cap:
                self.removeLast()
            newnode = node(value)
            self.moveToTop(newnode)
            self.map[key] = newnode
            self.sz += 1


    def moveToTop(self, node: node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    def removeLast(self):
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        last.prev = None
        last.next = None



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
