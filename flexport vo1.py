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


def findLongestCons(root: Node):
    result = [root, root, 1]  # (start_node, end_node, len)
    temp_res = [root, root, 1]  # (start_node, end_node, len)

    backtrack(root, result, temp_res)

    return result[2]


def proc(result):
    res = []
    n = result[1]
    while n is not result[0]:
        res.append(n.v)
        n = n.p

    res.append(n.v)
    res.reverse()
    return res


def matchPattern(c):
    if c.p:
        return c.v == c.p.v + 1


from copy import deepcopy


def backtrack(root, result, temp_res):
    # for each step , check child, if match pattern, we add to temp_res.
    #        1. set end_node
    #        2. increase len
    # if not match pattern, temp_res will be:
    #        1. compare w/ final res.
    #        2. temp_res set to initial.
    #
    # after comparing, we backtrack by shrink the temp_res.

    print(temp_res[0].v, temp_res[1].v, temp_res[2])
    if root == None:
        return

    for c in root.c:
        temp_res_copy = deepcopy(temp_res)
        if matchPattern(c):
            # update temp_res
            temp_res_copy[1] = c
            temp_res_copy[2] += 1

            # compare temp_res w/ final res
            if result[2] < temp_res[2]:
                result = temp_res

            backtrack(c, result, temp_res_copy)
        else:
            # refresh temp_res
            temp_res_copy = [c, c, 1]
            backtrack(c, result, temp_res_copy)


"""
 1
2 3
"""

n1 = Node(None, 1)

n2 = Node(n1, 2)
n3 = Node(n1, 3)

n1.c = [n2, n3]

print(findLongestCons(n1))



