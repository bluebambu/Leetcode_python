from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


# score: 
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(lambda : 0)
        for cpd in cpdomains:
            cnt, full_domain = cpd.split(' ')
            cnt = int(cnt)

            domain_lvls = full_domain.split('.')

            partial_path = ''
            for lvl in reversed(domain_lvls):
                partial_path = lvl + partial_path
                res[partial_path] += cnt
                partial_path = '.' + partial_path

        return [ (str(v) + ' ' + k) for k, v in res.items()]


tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.subdomainVisits(["9001 discuss.leetcode.com"])
print(r)
