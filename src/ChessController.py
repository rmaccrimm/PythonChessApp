# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from ChessPiece import *

class ChessController():
    
    def __init__(self, gui):
        self.chessGrid = {}
        self.gui = gui
        self.gui.addListener(self)
        self.currentPiece = None
        for i in range(8):
            for j in range(8):
                key = chr(i+97) + str(j+1)
                self.chessGrid[key] = None
            
    def notify(self, position):
        """Recieves the name of the cell clicked in the GUI"""
        print(position)
        
    def addPiece(self, position, piece):
        """Adds a piece at the given position. Cell must be empty before adding
        """
        try:
            if self.chessGrid[position] == None:
                self.chessGrid[position] = piece
                self.gui.drawPiece(piece.image)
            else:
                raise RuntimeError('Cell already occupied')
        except TypeError:
            print('Tried adding to non-existent cell')
            
    
    def removePiece(self, piece):
        pass
        
