from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        self.sort(intervals)
        headPos = self. find_insert_head_binary_srch(intervals, newInterval)
        tailPos = self. find_insert_tail_binary_srch(intervals, newInterval)
        return self. combine(intervals, headPos, tailPos, newInterval)

    def sort(self, intevals):
        pass

    def find_insert_head_binary_srch(self, intervals, newInterval):
        pass

    def combine(self, intervals, headPos, tailPos, newInterval):
        pass

    def find_insert_tail_binary_srch(self, intervals, newInterval):
        pass


