from collections import defaultdict
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node

# score:
class UnionFind:
    def __init__(self, size, relations:List):
        self.rootArr = [i for i in range(size)]
        for r in relations:
            frm, to = r[0], r[1]
            rFrm, rTo = self.find(frm), self.find(to)
            if rFrm != rTo:
                self.unify(rFrm, rTo)

    def find(self, i):
        while self.rootArr[i] != i:
            self.rootArr[i] = self.rootArr[self.rootArr[i]]
            i = self.rootArr[i]
        return i

    def unify(self, frm, to):
        rFrm, rTo = self.find(frm), self.find(to)
        if rFrm == rTo:
            return
        self.rootArr[frm] = to

    def isSameGroup(self, n1, n2):
        return self.find(n1) == self.find(n2)

    def findRoot(self, n):
        return self.find(n)

    def listGroups(self):
        s = set()
        for r in range(len(self.rootArr)):
            s.add(self.find(r))
        return s


uf = UnionFind(5, [[0,1], [0,2], [3,4]])
print(uf.listGroups())
print(uf.isSameGroup(0,3))
print(uf.isSameGroup(1,2))


