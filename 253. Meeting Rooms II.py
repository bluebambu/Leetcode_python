from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score:  15%
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = defaultdict(int)
        for intvl in intervals:
            times[intvl[0]] += 1
            times[intvl[1]] -= 1

        concurRoom = 0
        maxRoom = 0
        for time in sorted(times):
            meeting = times[time]
            concurRoom += meeting
            if concurRoom > maxRoom:
                maxRoom = concurRoom

        return maxRoom


s = Solution()
r = s.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
print(r)
r = s.minMeetingRooms([[7,10],[2,4]])
print(r)
