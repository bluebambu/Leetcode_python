from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        l = [1]*n
        cnt = [1]*n

        for i in range(1, n):
            cur_longest = 1
            cur_cnt = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if l[j]+1 > cur_longest:
                        cur_longest = l[j]+1
                        cur_cnt = cnt[j]
                    elif l[j]+1 == cur_longest:
                        cur_cnt = cur_cnt + cnt[j]
            l[i] = cur_longest
            cnt[i] = max(1, cur_cnt)

        print(l)
        print(cnt)
        maxl = max(l)
        r = 0
        for i, c in enumerate(cnt):
            if l[i] == maxl:
                r += c
        return r


s = Solution()
arr = [2,2,2,2,2]
print(arr)
r = s.findNumberOfLIS(arr)
print(r)
assert r == 5

arr = [1,3,5,4,7]
print(arr)
r = s.findNumberOfLIS(arr)
print(r)
assert r == 2



