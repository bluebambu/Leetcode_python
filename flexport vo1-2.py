
"""
      -2

      7

  8   3   -1

3  9


Return the longest list of consecutive integers in the tree.
Example: [7,8,9]

We are trying to find a pattern between a parent and a child in the tree.

Pattern: c = p + 1


"""


class Node:
    def __init__(self, parent, value):
        self.p = parent
        self.v = value
        self.c = []


from copy import deepcopy

global_res = [None, None, 1]

def findLongestCons(root: Node):
    dp(None, root, [])
    global global_res
    return global_res


def dp(parent: Node, cur: Node, temp_res):
    if not cur:
        return

    if parent == None:
        temp_res = [cur.v, cur.v, 1]
    elif parent.v + 1 == cur.v:
        temp_res[1] = cur.v
        temp_res[2] += 1
    else:
        temp_res = [cur.v, cur.v, 1]

    global global_res
    if global_res[2] < temp_res[2]:
        global_res = temp_res

    print("cur: " + str(cur.v), temp_res, global_res)
    for c in cur.c:
        dp(cur, c, []+temp_res)





"""
 1
2 3 4
##44##
 56
6
"""

n1 = Node(None, 1)
n2 = Node(n1, 2)
n3 = Node(n1, 3)
n4 = Node(n1, 4)
n1.c = [n2, n3, n4]

n5 = Node(n3, 4)
n6 = Node(n3, 4)
n3.c = [n5, n6]

n7 = Node(n5, 5)
n8 = Node(n5, 6)
n5.c = [n7, n8]

n9 = Node(n7, 6)
n7.c = [n9]


print(findLongestCons(n1))

