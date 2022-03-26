from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
#  第一题是给一个word列表，和一个string， 返回列表中能用string里面字符构造的word，找到一个就可以返回
def findWord(words:list, chars:str):
    charmap = defaultdict(lambda:0)
    for c in chars:
        charmap[c] += 1

    for w in words:
        if canFind(w, charmap):
            return True

    return False

def canFind(w:str, charmap: map):
    wmap = defaultdict(lambda :0)
    for c in w:
        wmap[c] += 1

    for k in wmap:
        cnt = wmap[k]

        if cnt > charmap[k]:
            return False

    return True



