from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# 第二题是消消乐。input: 一个整型的二维数组，出发点（x, y）。output：上下左右连的话，最终能消多少个点。比如：
grid = [
    [5,5,5,1,1],
    [1,1,5,2,1],
    [1,5,5,1,1],
]
#
# 出发点如果是(1,2)，则返回6。因为
# (5),(5),(5), 1, 1
# 1, 1,(5), 2, 1
# 1,   (5), (5), 1, 1

def findSameChar(grid, x, y):
    c = grid[x][y]
    return dfs(grid, x, y, c)

def dfs(grid, x, y, c:str):
    res = 0
    if grid[x][y] == c:
        grid[x][y] = 'x'
        res += 1
        for xx, yy in ((x+1, y), (x-1, y), (x, y+1), (x,y-1)):
            if 0<=xx<len(grid) and 0<=yy<len(grid[0]):
                res += dfs(grid, xx, yy, c)

    return res

print(findSameChar(grid, 1,2)) # == 6
print(findSameChar(grid, 1,0)) # ==3
print(findSameChar(grid, 1,3)) # ==1
