from typing import List
from XiangUtils.xiangUtils import Tree


# score:


def winner(arr):
    case1 = arr.head() - winner(arr.ridHead())
    case2 = arr.tail() - winner(arr.ridTail())
    return max(case1, case2)


DIRs = []

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacif = [[0 for i in range(n)] for j in range(m)]
        atlan = [[0 for i in range(n)] for j in range(m)]

        self.find_pacif_lands(heights, pacif)
        self.find_atlan_lands(heights, atlan)

        return self.find_both_lands(pacif, atlan)

    def find_pacif_lands(self, heights, pacif):
        m, n = len(heights), len(heights[0])
        que = []
        for i in range(n):
            que.append([0, i])
            pacif[0][i] = 1
        for i in range(1, m, 1):
            que.append([i, 0])
            pacif[i][0] = 1

        while que:
            x, y = que.pop(0)
            for d in DIRs:
                xx, yy = x+d[0], y+d[1]
                if 0<=xx<m and 0<=yy<n and pacif[xx][yy] and heights[xx][yy] >= heights[x][y]:
                    pacif[xx][yy] = 1
                    que.append([xx][yy])

class TwoSum:
    # 1. get 2 values
    # 2. get 2 index
    # 3. get all index
    # 4. get boolean
    # 5. not use hashmap
    def twoSum(self, list: List, target: int):
        valueSet = set()
        res = []
        for num in list:
            diff = target - num
            if diff in valueSet:
                res.append([diff, num])
            valueSet.add(num)

        return res
        # O(N)

    def twoSum2(self, list: List, target: int):
        pass
        # iterate 1, binary find another
        # O(NlgN)

    def twoSum3(self, list: List, target: int):
        sz = len(list)
        l, r = 0, sz-1
        res = []
        while l < r:
            small, large = list[l], list[r]
            if small + large < target:
                l += 1
            elif small + large > target:
                r -= 1
            else:
                res.append([l,r])
                l+=1
                r-=1
        return res


class BinarySearch:
    def find(self, arr:list, tgt):
        arr.sort()
        l, r = 0, len(arr)
        while l < r - 1:
            mid = int((r-l)/2) + l
            if arr[mid] <= tgt:
                l = mid
            else:
                r = mid

        return l

b = BinarySearch()
arr = [2,2,3,5,6,7,8,9]
i = b.find(arr, 9)
print(i)
print(arr[i])
