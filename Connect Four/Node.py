
class Node:
   def __init__(self,board,parent):
        self.board = board
        self.children = []
        self.parent = parent
        self.value = 0