from typing import List
from XiangUtils.xiangUtils import Tree


# score: 40%
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        def dfs(nums, i, path, r):
            if i == len(nums):
                r.append([]+path)
                return

            if not (path and path[-1] == nums[i]):
                dfs(nums, i+1, path, r)

            path.append(nums[i])
            dfs(nums, i+1, path, r)
            path.pop()

        dfs(nums, 0, [], r)
        return r



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.subsetsWithDup([1,1,2,2])
print(r)
