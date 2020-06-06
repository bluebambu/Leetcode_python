import collections


# use defaultdict to simplify add() methods
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
class WordDictionary2(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])


# 27.71%
class Node:
    def __init__(self):
        self.isWord = False
        self.child = [None] * 26
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        if word == '':
            return
        self.add(word, 0, self.root)

    def add(self, word, i, node):
        if i == len(word):
            node.isWord = True
            return
        c: str = word[i]
        x: int = ord(c) - ord('a')
        if node.child[x] == None:
            node.child[x] = Node()
        next = node.child[x]
        self.add(word, i+1, next)

    def search(self, word: str) -> bool:
        return self.s(word, 0, self.root)

    def s(self, word, i, node):
        if i == len(word):
            return node.isWord
        c = word[i]
        if c == '.':
            for next in node.child:
                if next and self.s(word, i+1, next):
                    return True
            return False
        else:
            x = ord(c) - ord('a')
            next = node.child[x]
            if next == None:
                return False
            else:
                return self.s(word, i+1, next)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    s = WordDictionary()
    s.addWord("bad")
    s.addWord("dad")
    s.addWord("mad")
    assert s.search("pad") == False
    assert s.search("bad") == True
    assert s.search(".ad") == True
    assert s.search("b..") == True