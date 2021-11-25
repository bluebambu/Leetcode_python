from collections import defaultdict

from XiangUtils.xiangUtils import Tree, DoubleLinkedList


# score:
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container: DoubleLinkedList = DoubleLinkedList()
        self.maxList = defaultdict(lambda : [])

    def pushList(self, l: list):
        """
        initialize your data structure here.
        """
        for e in l:
            self.push(e)

    def push(self, x: int) -> None:
        ref = self.container.append(x)
        self.maxList[x].append(ref)

    def pop(self) -> int:
        top = self.container.pop()
        if top is None:
            return None
        self.maxList[top.val].remove(top)
        if len(self.maxList[top.val]) == 0:
            self.maxList.pop(top.val)
        return top.val


    def top(self) -> int:
        top = self.container.tailNode()
        if top is None:
            return None
        return top.val

    def peekMax(self) -> int:
        if len(self.maxList) == 0:
            return None
        max_key = max(self.maxList.keys())
        return max_key

    def popMax(self) -> int:
        if len(self.maxList.keys()) == 0:
            return None
        max_key = max(self.maxList.keys())
        if len(self.maxList[max_key]) == 0:
            return None
        ref = self.maxList[max_key][-1]
        self.maxList[max_key].pop()
        if len(self.maxList[max_key]) == 0:
            self.maxList.pop(max_key)
        self.container.removeNode(ref)
        return ref.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')

st = MaxStack()
print(st.peekMax())
print(st.top())
print('*'*20)

st.push(1)
print(st.peekMax())
print(st.top())
print(st.pop())
print(st.pop())
print(st.popMax())
print('*'*20)

st.push(1)
print(st.popMax())
print(st.top())
print(st.pop())
print(st.pop())
print(st.popMax())
print('*'*20)

st.pushList([1,3,2,5,3,4,5,2])
print(st.peekMax())
print(st.top())
print(st.popMax())
print(st.popMax())
print(st.peekMax())
print(st.popMax())
print(st.peekMax())
print(st.popMax())
print(st.popMax())
print(st.popMax())
print(st.popMax())
print(st.popMax())
print(st.popMax())
print(st.popMax())

