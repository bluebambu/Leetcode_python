from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node


class Piece(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.p = None

    def tryMove(self, new_x, new_y):
        pass

class Cat(Piece):
    def __init__(self):
        super(self)

    def tryMove(self, new_x, new_y):
        '''
        1. check if same row or same col
        2. check if distance > 3
        3. check if there is friend chess on route:
            how: use for loop : [x, y->new_y] or [x->new_x, y] and check.
        4. check if new pos is the same as old pos
        5. return True or False

        '''

class Player(object):
    def tryMove(self, old_x, old_y, new_x, new_y, board):
        '''
        1. if not this player's chess, return  false
        '''

        piece: Piece = board[old_x][old_y]
        return piece.tryMove(new_x, new_y)


class Status:
    UNSTARTED = 0
    STARTED = 1
    FINISHED = 2


def getPlayerInput():
    pass


class Game:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.curP = True

        self.board = [[None for i in range(7)] for i in range(7)]

        self.status = Status.UNSTARTED

    def run(self):
        while self.status != Status.FINISHED:
            cur_round = True
            cur_player = self.p1 if self.curP else self.p2
            while cur_round:
                old_x, old_y, new_x, new_y = getPlayerInput()
                if cur_player.tryMove(old_x, old_y, new_x, new_y, self.board):
                    cur_player.move(old_x, old_y, new_x, new_y, self.board)
                    cur_round = False
                else:
                    print("Invalid move, try again.")

            if checkFinished():
                self.status = Status.FINISHED




