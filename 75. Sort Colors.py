from typing import List


# score: 5%
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        id0, id2 = 0, len(nums)-1
        i = 0
        while i <= id2:
            if nums[i] == 0:
                nums[i], nums[id0] = nums[id0], nums[i]
                i+=1
                id0 +=1
            elif nums[i] == 2:
                nums[i], nums[id2] = nums[id2], nums[i]
                id2 -= 1
            else:
                i+=1
        print(nums)



s = Solution()
r = s.sortColors([2,0,2,1,1,0])
r = s.sortColors([2,0,1])
