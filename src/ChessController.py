# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from ChessPiece import *
import itertools


class ChessController(object):
    """Handles chess game logic and updates ChessGui
    """
    
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
        """Places the initial pieces on the board.
        """
        colors = itertools.cycle(['white', 'black'])
        rows = itertools.cycle([1,8])
        for i in range(2):
            color = next(colors)
            row = str(next(rows))
            self.addPiece('a'+row, Rook(color))
            self.addPiece('h'+row, Rook(color))
            self.addPiece('b'+row, Knight(color))
            self.addPiece('g'+row, Knight(color))
            self.addPiece('c'+row, Bishop(color))
            self.addPiece('f'+row, Bishop(color))
            self.addPiece('d'+row, King(color))
            self.addPiece('e'+row, Queen(color))
        for i in range(8):
            self.addPiece(chr(97+i)+str(2), Pawn('white'))
            self.addPiece(chr(97+i)+str(7), Pawn('black'))
            
    def notify(self, position):
        """Recieves the name of the cell clicked in the GUI. Redirects input 
        to movePieces function
        """
        self.movePieces(position)
    
    def movePieces(self, position):
        """Defines the behaviour for each input. First input stores a piece to
        be moved. Second input
            a) moves the piece if the cell is empty or contains opposite color.
            b) selects a new piece to move, if same color as stored piece.
            c) cancels the move, if same piece.
        """
        print(position)
        if self.currentPiece == None:
            self.setCurrent(position)
        else:
            if position != self.currentCell:
                piece = self.chessGrid[position]
                if piece == None or piece.color != self.currentPiece.color:
                    self.removePiece(position)  
                    self.addPiece(position, self.currentPiece)
                    self.removePiece(self.currentCell)
                    self.currentPiece = None
                    self.currentCell = None
                else:
                    self.setCurrent(position)
            else:
                self.currentPiece = None
                self.currentCell = None
                    
    def setCurrent(self, position):
        """Stores the selected piece and position to be moved on the next input.
        """
        try:
            self.currentPiece = self.chessGrid[position]
            self.currentCell = position
        except KeyError:
            print('Position does not exist')
            
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
        """Remove piece from the given position.
        """
        try:
            if self.chessGrid[position] != None:
                self.gui.removePiece(position)
                self.chessGrid[position] = None
        except (KeyError, RuntimeError) as e:
            print('No piece to remove')
            
        
