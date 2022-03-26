# There are colorful tokens in red, blue, green and so on , and a person may own some of these tokens;
# A card can be purchased by tokens, just different types of cards my require different amount of different
# colored tokens (e.g. 2 blue and 2 green tokens can buy a type of card, and 1 red and 2 blue tokens can buy another type of card, etc)
# 然后你开始设计一些class来实现这个情景，面试官一次提出一个功能
#
# 让你实现，大部分就是在某些class里实现canPurchase()， makePurchase()这些功能。class有哪些field property、用什么数据结构都是开放性自主选择，被问到了解释下原因就好。
# 注意是你自己写tests来跑。测试通过一个功能再move on下一个需求。
from collections import defaultdict


class Token:
    def __init__(self, color:str):
        self.color = color

class Card:
    def __init__(self, cardType:str):
        self.cardType = cardType

class People:
    def __init__(self):
        self.pocket = defaultdict(lambda : 0)

    def addToken(self, t:Token, n:int):
        self.pocket[t.color] += n

    def makePurchase(self, cost: map):
        pass