# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
import itertools
from ChessCell import *

class ChessGui():
    
    def __init__(self, root):
        self.chessGrid = {}
        self.root = root
        self.squareLength = 60
        self.currentPiece = None
        colorIter = itertools.cycle(['black', 'white'])
        
        for i in range(8):
            for j in range(8):
                key = chr(i+97) + str(j+1)
                self.chessGrid[key] = ChessCell(self.root, row=8-i, column=j,
                                                color=next(colorIter))
                self.chessGrid[key].canvas.bind('<Button-1>', 
                    lambda event, position=key: self.movePiece(event, position))
            next(colorIter)
            
    def initPieces(self):
        self.chessGrid['a1'].add()
        
    def movePiece(self, event, position):
        print(position)