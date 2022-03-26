from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
NUM_TO_CH_MAP2 = {
    '1': ['a', 'b'],
    '2': ['c', 'd'],
    '11': ['x']
}


# dfs algo
def numMapping2(s: str) -> List[str]:
    if not s:
        return []

    #
    path = [""]

    # all paths
    res = []

    #
    dfs(s, path, res)

    return res


def dfs(s, path, res) -> None:
    # dfs ends here
    if not s:
        for s2 in path:
            res.append(s2)
        return

    #
    for i, c in enumerate(s):
        cur_str = s[:i + 1]

        if cur_str not in NUM_TO_CH_MAP2:
            continue

        mapping = NUM_TO_CH_MAP2[cur_str]

        new_path = []
        for existing_str in path:
            for cur_candidate in mapping:
                new_str = existing_str + cur_candidate
                new_path.append(new_str)

        dfs(s[i + 1:], new_path, res)


print(numMapping2('1'))
print(numMapping2('11'))
print(numMapping2('111'))
