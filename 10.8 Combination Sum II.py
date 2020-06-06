from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(0, candidates, 0, target, [], res)
        return res

    def dfs(self, st, cands, sum, tgt, coll, res):
        if st == len(cands):
            if sum == tgt:
                res.append(coll[:]) # append() is using ref, not copy
            return

        if len(coll)==0 or coll[-1] != cands[st]:
            self.dfs(st+1, cands, sum, tgt, coll, res)

        coll.append(cands[st])
        self.dfs(st+1, cands, sum+cands[st], tgt, coll, res)
        coll.pop()

s = Solution()
res = s.combinationSum2([10,1,2,7,6,1,5], 8)
print(res)
assert res == [
  [2, 6],
  [1, 7],
  [1, 2, 5],
  [1, 1, 6]
]

