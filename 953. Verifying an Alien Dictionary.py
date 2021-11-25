from typing import List
from XiangUtils.xiangUtils import Tree


# score: 89.1%
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alp = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            cur, nxt = words[i], words[i+1]
            if not self.isSmall(cur, nxt, alp):
                return False

        return True

    def isSmall(self, a, b, alp):
        for i in range(min(len(a), len(b))):
            Achar, Bchar = a[i], b[i]
            if alp[Achar] > alp[Bchar]:
                return False
            elif alp[Achar] < alp[Bchar]:
                return True

            if i == len(b) - 1 and i < len(a) - 1:
                return False

        return True



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
r = s.isAlienSorted(words, order)
print(r)


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
r = s.isAlienSorted(words, order)
print(r)


words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
r = s.isAlienSorted(words, order)
print(r)
