from collections import defaultdict
from typing import List
from collections import deque
from xiangUtils import TreeNode, Tree, lvlOrder

# score:  70%
class Solution:
    def wordPatternMatch(self, pattern: str, words: str) -> bool:
        p2w = {}
        w2p = {}
        def dfs(pattern, i, words, j):
            if i == len(pattern):
                return j == len(words)

            p = pattern[i]
            if p in p2w:
                exist = p2w[p]
                if words[j:j+len(exist)] == exist:
                    return dfs(pattern, i+1, words, j+len(exist))
                else:
                    return False
            else:
                for jj in range(j, len(words)):
                    newWord = words[j:jj+1]
                    if newWord in w2p and w2p[newWord]!=p:
                        continue

                    p2w[p] = newWord
                    w2p[newWord] = p
                    if dfs(pattern, i+1, words, j+len(newWord)):
                        return True
                    else:
                        p2w.pop(p)
                        w2p.pop(newWord)
                return False

        return dfs(pattern, 0, words, 0)



tree = Tree('1,2,3,4,#,2,4,#,#,4,#,#,#,#,#')
s = Solution()
r = s.wordPatternMatch('abab', 'redblueredblue')
print(r)
r = s.wordPatternMatch('aaaa', 'asdasdasdasd')
print(r)
r = s.wordPatternMatch('aabb', 'xyzabcxzyabc')
print(r)
r = s.wordPatternMatch('ab', 'aa')
print(r)
