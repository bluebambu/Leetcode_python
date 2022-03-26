from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_itvls = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] <= newInterval[0]:
                new_itvls.append(intervals[i])
                i+=1
            else:
                break

        merge(new_itvls, newInterval)

        while i < len(intervals):
            merge(new_itvls, intervals[i])
            i += 1

        return new_itvls

def merge(intervals: List[List[int]], intvl: List[int]):
    # only merge the intvl w/ last of intervals
    if len(intervals) == 0:
        intervals.append(intvl)
        return

    last_intvl = intervals[-1]
    if intvl[0] > last_intvl[1]:
        intervals.append(intvl)
    else:
        intervals[-1][1] = max(intervals[-1][1], intvl[1])


s = Solution()
new = s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
print(new)






