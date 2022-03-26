"""
this is a good sentence and this is a bad sentence
"""
from collections import defaultdict
from random import randrange


class randomGenerator2:
    def __init__(self, s: str):
        self.l = s.split(' ')
        self.len = len(self.l)
        self.m = self.genWordIndexMap(self.l)
        self.lastGenWord = None
        self.roundNum = 0

    def getNextRandomWord(self):
        if self.lastGenWord is None:
            self.lastGenWord = self.getRandom2Words(self.l)
            self.roundNum += 1
            return self.lastGenWord
        else:
            lastGenWordIndices: list = self.m[self.lastGenWord]
            nextWordIndices = [(i + 2) % self.len for i in lastGenWordIndices]
            print("\t candidates include: " + ','.join([self.l[w] for w in nextWordIndices]))
            chosenNextIdx = randrange(0, len(nextWordIndices))
            self.lastGenWord = self.lastGenWord.split(' ')[1] + ' ' + self.l[nextWordIndices[chosenNextIdx]]
            self.roundNum += 1
            return self.lastGenWord

    def genWordIndexMap(self, l):
        m = defaultdict(lambda: [])
        for i, w in enumerate(l):
            twoW = l[i]+' '+l[(i+1)%self.len]
            m[twoW].append(i)
        return m

    def getRandom2Words(self, l):
        i = randrange(0, len(l))
        return l[i]+' '+l[(i+1)%len(l)]


gen = randomGenerator2("this is a good sentence and this is a bad sentence and that is a nice sentence")
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
print(gen.getNextRandomWord())
