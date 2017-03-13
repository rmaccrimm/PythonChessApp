# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from chessApp.chessPieces import *
import itertools
from chessApp.moveGenerator import getPossible


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

    def getPositions(self):
        """Returns a list containing the positions of every piece on the board
        """
        positions = [pos for pos in self.chessGrid 
                     if self.chessGrid[pos] != None]
        return positions
    
    def getPieces(self):
        """Returns a dictionary containing all the pieces on the board
        """
        pieces = {pos:self.chessGrid[pos] for pos in self.getPositions()}
        return pieces
    
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
    
    def handleClick(self, position):
        """Defines the behaviour for each input. First input stores a piece to
        be moved. Second input
            a) moves the piece if the cell is empty or contains opposite color.
            b) stores a new piece to move if same color as current stored piece.
            c) cancels the move if same piece.
        """
        if self.currentPiece == None:
            if self.chessGrid[position] != None:
                self.setCurrent(position)
        elif position != self.currentCell:
            piece = self.chessGrid[position]
            possible = getPossible(self.getPieces(), self.currentCell)
            if piece == None:
                if position in possible:
                    self.addPiece(position, self.currentPiece)
                    self.removePiece(self.currentCell)
                    self.setCurrent(None)
                else:
                    print('Invalid Move')
            elif piece.color != self.currentPiece.color:
                if position in possible:
                    self.removePiece(position)  
                    self.addPiece(position, self.currentPiece)
                    self.removePiece(self.currentCell)
                    self.setCurrent(None)
                else:
                    print('Invalid move')
            else: 
                print('Invalid move')
        else:
            self.setCurrent(None)
                    
    def setCurrent(self, position):
        """Stores the selected piece and position to be moved on the next input.
        """
        if position == None:
            self.currentPiece = None
            self.currentCell = None
        else:
            if isinstance(position, str):
                self.currentPiece = self.chessGrid[position]
                self.currentCell = position
            else:
                raise TypeError('Position must be a string')
            
    def addPiece(self, position, piece):
        """Adds a piece at the given position. Cell must be empty before adding
        """
        if isinstance(piece, ChessPiece):
            if self.chessGrid[position] == None:
                self.chessGrid[position] = piece
                self.gui.drawPiece(position, piece.image)
            else:
                raise RuntimeError('Cell already occupied')
        else:
            raise TypeError('Added piece is not derived from ChessPiece')
                
            
    def removePiece(self, position):
        """Remove piece from the given position.
        """
        if self.chessGrid[position] != None:
            self.gui.removePiece(position)
            self.chessGrid[position] = None
        else:
            raise RuntimeError('No piece to remove')