from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score: 42%
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        r = []
        def dfs(nums, path, visited, r):
            if len(path) == len(nums):
                r.append([]+path)
                return
            curV = set()
            for idx, v in enumerate(nums):
                if idx not in visited and v not in curV:
                    path.append(v)
                    curV.add(v)
                    visited.add(idx)
                    dfs(nums, path, visited, r)
                    visited.remove(idx)
                    path.pop()

        dfs(nums, [], set(), r)
        return r

# score: 30%
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        def dfs(nums, i, r):
            if i == len(nums):
                r.append([]+nums)
                return
            vset = set()
            for j in range(i, len(nums)):
                if nums[j] not in vset:
                    vset.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    dfs(nums, i+1, r)
                    nums[i], nums[j] = nums[j], nums[i]

        dfs(nums, 0, r)
        return r

tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution2()
r = s.permuteUnique([1,1,2])
print(r)
