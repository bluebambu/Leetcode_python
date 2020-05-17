from collections import deque, defaultdict
from typing import List

# pass , 7.71%
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        chMap = {}
        indeg = {}
        queue = deque()
        for i in range(len(words)-1):
            l, h = self.proc(words[i], words[i+1])
            if l==-1 and h==-1:
                return ''
            if l==None:
                continue
            chMap.setdefault(l, set()).add(h)

        for low, highs in chMap.items():
            for h in highs:
                indeg[h] = indeg.get(h, 0) + 1

        allch = set(''.join(words))
        for c in allch:
            if indeg.get(c, 0) ==0:
                queue.append(c)

        res = []
        while len(queue) != 0:
            f = queue.popleft()
            res.append(f)
            for h in chMap.get(f, set()): # 要注意终点不要出现 keyError
                indeg[h]-=1
                if indeg[h]==0:
                    queue.append(h)

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


# fastest impl
class Solution2:
    def alienOrder(self, words: List[str]) -> str:
        def build_graph(words):
            graph = defaultdict(list)
            indeg = defaultdict(int)

            for w1, w2 in zip(words, words[1:]):
                isTie = True
                for c1, c2 in zip(w1, w2):
                    if c1!=c2:
                        graph[c1].append(c2)
                        indeg[c2]+=1
                        isTie=False
                        break

                if isTie and len(w1)>len(w2):
                    return None, None, False

            return graph, indeg, True

        def bfs(graph, indeg, char_set):
            queue = [c for c in char_set if indeg[c]==0]
            res = []

            while queue:
                next_q = []
                for c in queue:
                    res.append(c)

                    for neighbor in graph[c]:
                        indeg[neighbor] -= 1
                        if indeg[neighbor] == 0:
                            next_q.append(neighbor)
                queue = next_q

            return "".join(res)

        g, ind, isValid = build_graph(words)

        char_set = set([c for word in words for c in word])

        if not isValid:
            return ""

        res = bfs(g, ind, char_set)

        if len(res) != len(char_set):
            return ''
        else:
            return res

if __name__ == '__main__':
    s = Solution2()
    words = ["wrt", "wrf", "er", "ett", "rftt" ]
    res = s.alienOrder(words)
    assert res == "wertf"
    words2 = [ "z", "x", "z" ]
    assert res == ""
    words3 = [ "z", "z" ]
    assert s.alienOrder(words3) == 'z'
    words4 = ["wrt","wrf","er","ett","rftt"]
    assert s.alienOrder(words4) == "wertf"

