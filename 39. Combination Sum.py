from typing import List


# score:  22%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        r = []
        def dfs(cands, i, path, tgt, r):
            if tgt < 0:
                return
            if tgt == 0:
                r.append([]+path)
                return
            for j in range(i, len(cands)):
                path.append(cands[j])
                dfs(cands, j, path, tgt-cands[j], r)
                path.pop()

        dfs(candidates, 0, [], target, r)
        return r


s = Solution()
r = s.combinationSum([2,3,6,7], 7)
print(r)
