from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(str(num))
        bucket = [-1 for i in range(10)]

        for i, c in enumerate(l):
            bucket[int(c)] = i

        for i, c in enumerate(l):
            cur_num = int(c)
            j = 9
            while j > cur_num:
                if bucket[j] != -1 and bucket[j] > i:
                    pos = bucket[j]
                    l[i], l[pos] = l[pos], l[i]
                    return int(''.join(l))
                j -= 1

        return num


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.maximumSwap(2736)
print(r)
