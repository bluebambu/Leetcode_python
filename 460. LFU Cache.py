from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque


# score:
class Node:
    def __init__(self, k=None, v=None):
        self.key = k
        self.value = v
        self.cnt = 0
        self.prv = None
        self.nxt = None


class LL:
    def __init__(self):
        self.head, self.tail  = Node(), Node()
        self.head.nxt = self.tail
        self.tail.prv = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0


class LFUCache:
    def __init__(self, capacity: int):
        self.keyMap = {}
        self.freqMap = defaultdict(lambda :LL())
        self.size = 0
        self.cap = capacity
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        n = self.keyMap[key]
        v = n.value
        self.nodeCntPlus1(n)
        return v

    def put(self, key: int, value: int) -> None:
        if key not in self.keyMap:
            if self.size == self.cap:
                # remove lease recent, lease freq node
                if self.minfreq not in self.freqMap:
                    raise Exception("minfreq not exist")

                min_LL = self.freqMap[self.minfreq]
                n = min_LL.head.nxt
                k = n.key
                min_LL.popLeft()
                self.keyMap.pop(k, None)

            self.keyMap[key] = Node(key, value)
            n = self.keyMap[key]
            n.cnt = 1
            self.minfreq = 1
            self.freqMap[1].append(n)
            self.size += 1
        else:
            n = self.keyMap[key]
            n.value = value
            self.nodeCntPlus1(n)

    def nodeCntPlus1(self, n):
        old_c, k = n.cnt, n.k
        old_LL = self.freqMap[old_c]
        old_LL.pop(n)
        n.cnt += 1
        new_LL = self.freqMap[n.cnt]
        new_LL.append(n)

        if self.minfreq == old_c and old_LL.isEmpty():
            self.minfreq += 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


s = Solution()
r = s.canWin()
print(r)
assert r == True
