from collections import defaultdict


class Trie:
    class Node:
        def __init__(self):
            self.isWord = False
            self.children = defaultdict()

    def __init__(self):
        self.head = self.Node()

    def insert(self, word):
        ptr = self.head
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = self.Node()
            ptr = ptr.children[ch]
        ptr.isWord = True

    def find(self, word):
        ptr = self.head
        for ch in word:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return ptr.isWord


t = Trie()
t.insert("abb")
t.insert("acdbb")
print(t.find("abb"))
print(t.find("abc"))




