from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


class RateLimiter:
    '''
    leaking bucket
    '''
    def __init__(self):
        self.threthold = 3.0
        self.recoverRate = 3.0
        self.quotaPerReq = 1
        self.cntMap = defaultdict(lambda : (0.0, 3.0))

    def shouldAccept(self, ts:float, key):
        last_ts, quota = self.cntMap[key]

        time_diff = ts - last_ts
        quota = min(self.threthold, quota + self.recoverRate * time_diff)

        if quota < self.quotaPerReq:
            self.cntMap[key] = (ts, quota)
            return False
        else:
            quota -= self.quotaPerReq
            self.cntMap[key] = (ts, quota)
            return True

r = RateLimiter()
print(r.shouldAccept(0.1, 'a'))
print(r.shouldAccept(0.2, 'a'))
print(r.shouldAccept(0.3, 'a'))
print(r.shouldAccept(0.4, 'a'))
print(r.shouldAccept(0.4, 'b'))
print(r.shouldAccept(1.0, 'a'))


