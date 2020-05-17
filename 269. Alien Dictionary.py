from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""

        chset = set(''.join(words))
        allch = []
        for w in words:
            for c in w:
                if c in chset:
                    allch.append(c)
                    chset.remove(c)

        indeg = {}
        chMap = {}
        for i in range(len(words)-1):
            lowCh, highCh = self.proc(words[i], words[i+1])
            if lowCh==None and highCh==None:
                continue
            if lowCh==-1 and highCh==-1:
                return ""
            chMap.setdefault(lowCh, set()).add(highCh)

        for c in chMap:
            highs = chMap[c]
            for h in highs:
                indeg[h] = indeg.get(h, 0) + 1

        res = []
        [self.topo(indeg, chMap, c, res) for c in [x for x in allch if indeg.get(x, 0) == 0]]

        if len(res) != len(allch):
            return ""
        return ''.join(res)

    def proc(self, w1, w2):
        for i in range(len(w1)):
            if i >= len(w2):
                return -1, -1
            if w1[i] != w2[i]:
                return w1[i], w2[i]

        return None, None

    def topo(self, indeg, chMap, low, res: List):
        res.append(low)
        for high in chMap.get(low, set()):
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
words4 = ["wrt","wrf","er","ett","rftt"]
print(s.alienOrder(words4))

