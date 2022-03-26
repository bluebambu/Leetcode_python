from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# Part 2
# After catching your classroom students cheating before, you realize your students are getting craftier and
# hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be
# either immediately below or immediately to the right of the previous letter.
#
# Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates.
# If there are multiple matches, return any one.
grid1 = [
       ['c', 'c', 'x', 't', 'i', 'b'],
       ['c', 'c', 'a', 't', 'n', 'i'],
       ['a', 'c', 'n', 'n', 't', 't'],
       ['t', 'c', 's', 'i', 'p', 't'],
       ['a', 'o', 'o', 'o', 'a', 'a'],
       ['o', 'a', 'a', 'a', 'o', 'o'],
       ['k', 'a', 'i', 'c', 'k', 'i'],
   ]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

#find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
#find_word_location(grid1, word2) =>
#       [(0, 1), (1, 1), (2, 1), (3, 1)]
#      OR [(0, 0), (1, 0), (1, 1), (2, 1)]
#      OR [(0, 0), (0, 1), (1, 1), (2, 1)]
#      OR [(1, 0), (1, 1), (2, 1), (3, 1)]
#find_word_location(grid1, word3) => [(3, 2)]
#find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
#find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
#find_word_location(grid1, word6) => [(6, 4), (6, 5)]
#find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
#find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
#find_word_location(grid2, word9) => [(0, 0)]

#Complexity analysis variables:
#r = number of rows
#    c = number of columns
#w = length of the word
#
# Start from each position, DFS with backtracking for the word
# Time: O(r * c * 4 * 3^(w-1)) = O (r * c * 3^w)
# Space: O(1)

def find_word_location(grid:list, w:str) -> list:
    res = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if dfs(grid, x, y, w, 0, res):
                return res

    return res

visited = {}

def dfs(grid, x, y, w:str, wi:int, res) -> bool:
    if (x, y, wi) in visited:
        return visited[(x, y, wi)]

    c = grid[x][y]
    p = w[wi]
    z = (x, y)
    zz = res

    if c != p:
        return False

    res.append((x, y))
    if wi == len(w) - 1:
        return True

    for xx, yy in ((x+1, y), (x, y+1)):
        if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and dfs(grid, xx, yy, w, wi+1, res):
            return True

    res.pop()
    visited[(x, y, wi)] = False
    return False


print(find_word_location(grid1, word5) == [(4, 5), (5, 5), (6, 5)])
print(find_word_location(grid1, word3) == [(3, 2)])
print(find_word_location(grid1, word4) == [(0, 5), (1, 5), (2, 5)])
print(find_word_location(grid1, word5) == [(4, 5), (5, 5), (6, 5)])
print(find_word_location(grid1, word6) == [(6, 4), (6, 5)])
print(find_word_location(grid1, word7) == [(5, 1), (5, 2), (5, 3)])
print(find_word_location(grid1, word8) == [(4, 1), (4, 2), (4, 3)])
print(find_word_location(grid2, word9) == [(0, 0)])

