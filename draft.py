from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder, Node

# score:
def win(state):
    for avail in state.getAvail():
        next_state = getNext(state, avail)
        if not win(next_state):
            return True

    return False


def winner(arr):
    case1 = arr.head() - winner(arr.ridHead())
    case2 = arr.tail() - winner(arr.ridTail())
    return max(case1, case2)


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.canWin()
print(r)
assert r == True
