from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


def canWin(nums: str):
    if not nums:
        return False

    curChar = nums[0]
    cnt = 1

    for i in range(1, len(nums)):
        c = nums[i]
        if c == curChar:
            cnt += 1
        else:
            if cnt % 3 != 0:
                return False
            curChar = c
            cnt = 1

    return cnt == 2

print(canWin("11122"))
print(canWin("111"))
print(canWin("1112233"))
print(canWin("00000011"))
