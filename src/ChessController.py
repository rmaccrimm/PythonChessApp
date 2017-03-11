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
        self.currentCell = None
        for i in range(8):
            for j in range(8):
                key = chr(i+97) + str(j+1)
                self.chessGrid[key] = None
    
    def initPieces(self):
        for i in range(8):
            self.addPiece(chr(97+i)+str(2), WhitePawn())
            self.addPiece(chr(97+i)+str(7), BlackPawn())
        self.addPiece('b8', BlackKnight())
        self.addPiece('g8', BlackKnight())
        self.addPiece('a8', BlackRook())
        self.addPiece('h8', BlackRook())
        self.addPiece('c8', BlackBishop())
        self.addPiece('f8', BlackBishop())
        self.addPiece('d8', BlackKing())
        self.addPiece('e8', BlackQueen())
        self.addPiece('b1', WhiteKnight())
        self.addPiece('g1', WhiteKnight())
        self.addPiece('a1', WhiteRook())
        self.addPiece('h1', WhiteRook())
        self.addPiece('c1', WhiteBishop())
        self.addPiece('f1', WhiteBishop())
        self.addPiece('d1', WhiteKing())
        self.addPiece('e1', WhiteQueen())
            
    def notify(self, position):
        """Recieves the name of the cell clicked in the GUI"""
        print(position)
        if self.currentPiece == None:
            try:
                self.currentPiece = self.chessGrid[position]
                self.currentCell = position
            except KeyError:
                print('Position does not exist')
        else:
            self.removePiece(position)
            self.addPiece(position, self.currentPiece)
            self.removePiece(self.currentCell)
            self.currentPiece = None
            self.currentCell = None

    def addPiece(self, position, piece):
        """Adds a piece at the given position. Cell must be empty before adding
        """
        try:
            if self.chessGrid[position] == None:
                self.chessGrid[position] = piece
                self.gui.drawPiece(position, piece.image)
            else:
                raise RuntimeError('Cell already occupied')
        except TypeError:
            print('Tried adding to non-existent cell')
            
    def removePiece(self, position):
        try:
            if self.chessGrid[position] != None:
                self.gui.removePiece(position)
                self.chessGrid[position] = None
        except (KeyError, RuntimeError) as e:
            print('No piece to remove')
            
        
