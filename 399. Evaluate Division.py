from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""

        indeg = {}
        chMap = {}
        for i in range(len(words)-1):
            lowCh, highCh = self.proc(words[i], words[i+1], indeg, chMap)
            if lowCh==None and highCh==None:
                continue
            chMap.setdefault(lowCh, set()).add(highCh)
            chMap.setdefault(highCh, set())
            indeg[highCh] = indeg.get(highCh, 0) + 1
            indeg[lowCh] = indeg.get(lowCh, 0)

        res = []
        seed = [self.topo(indeg, chMap, i, res) for i in [k for k, v in indeg.items() if v == 0]]

        if [v for k, v in indeg.items() if v!=0] != []:
            return ""
        return ''.join(res)

    def proc(self, w1, w2, indeg, chMap):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return w1[i], w2[i]

        return None, None

    def topo(self, indeg, chMap, low, res: List):
        res.append(low)
        for high in chMap[low]:
            indeg[high] = indeg[high] - 1
            if indeg[high] == 0:
                self.topo(indeg, chMap, high, res)

s = Solution()
words = [ "wrt", "wrf", "er", "ett", "rftt" ]
res = s.alienOrder(words)
print(res)
words2 = [ "z", "x", "z" ]
print(s.alienOrder(words2))
words3 = [ "z", "z" ]
print(s.alienOrder(words3))

