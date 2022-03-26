"""
this is a good sentence and this is a bad sentence
"""
from collections import defaultdict
from random import randrange


class randomGenerator:
    def __init__(self, s: str):
        self.l = s.split(' ')
        self.len = len(self.l)
        self.m = self.genWordIndexMap(self.l)
        self.lastGenWord = None
        self.roundNum = 0

    def getNextRandomWord(self):
        if self.lastGenWord is None:
            self.lastGenWord = self.getRandomWord(self.l)
            self.roundNum += 1
            return self.lastGenWord
        else:
            lastGenWordIndices: list = self.m[self.lastGenWord]
            nextWordIndices = [(i + 1) % self.len for i in lastGenWordIndices]
            self.lastGenWord = self.l[self.getRandomWord(nextWordIndices)]
            self.roundNum += 1
            print("\t candidates include: " + ','.join([self.l[w] for w in nextWordIndices]))
            return self.lastGenWord

    def genWordIndexMap(self, l):
        m = defaultdict(lambda: [])
        for i, w in enumerate(l):
            m[w].append(i)
        return m

    def getRandomWord(self, l):
        i = randrange(0, len(l))
        return l[i]


gen = randomGenerator("this is a good sentence and this is a bad sentence and that is a nice sentence")
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
