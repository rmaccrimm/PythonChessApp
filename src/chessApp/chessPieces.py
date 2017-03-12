# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from PIL import Image
from chessApp.resources.images import *
from pkg_resources import resource_filename


class ChessPiece(object):
    """Stores an image and name for each type of chess piece. Later on will 
    handle move generation to check if moves are valid.
    """
    _bImage = None
    _wImage = None
    _name = None
    
    def __init__(self, color):
        if None in (self._bImage, self._wImage, self._name):
            raise NotImplementedError
        self.color = color
        if self.color == 'black':
            self._image = self._bImage
        elif self.color == 'white':
            self._image = self._wImage

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        value = value.lower()
        if value == 'black':
            self._color = value
        elif value == 'white':
            self._color = value
        else:
            raise ValueError('Color must be black or white')
        
    @property
    def image(self):
        return self._image
    
    @property
    def name(self):
        return self._name
    
    def movePossible(position):
        """Check if move is valid for the piece. To be implemented in the 
        future.
        """
        return True


class Pawn(ChessPiece):
    _bImage = Image.open(resource_filename('chessApp.resources.images',
                         'bPawn.png'))
    _wImage = Image.open(resource_filename('chessApp.resources.images',
                         'wPawn.png'))
    _name = 'pawn'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)


class Knight(ChessPiece):
    _bImage = Image.open(resource_filename('chessApp.resources.images',
                         'bKnight.png'))
    _wImage = Image.open(resource_filename('chessApp.resources.images',
                         'wKnight.png'))
    _name = 'knight'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)
  
        
class Rook(ChessPiece):
    _bImage = Image.open(resource_filename('chessApp.resources.images',
                         'bRook.png'))
    _wImage = Image.open(resource_filename('chessApp.resources.images',
                         'wRook.png'))
    _name = 'rook'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)
  
        
class Bishop(ChessPiece):
    _bImage = Image.open(resource_filename('chessApp.resources.images',
                         'bBishop.png'))
    _wImage = Image.open(resource_filename('chessApp.resources.images',
                         'wBishop.png'))
    _name = 'bishop'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)
 
        
class King(ChessPiece):
    _bImage = Image.open(resource_filename('chessApp.resources.images',
                         'bKing.png'))
    _wImage = Image.open(resource_filename('chessApp.resources.images',
                         'wKing.png'))
    _name = 'king'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)        
  
        
class Queen(ChessPiece):
    _bImage = Image.open(resource_filename('chessApp.resources.images',
                         'bQueen.png'))
    _wImage = Image.open(resource_filename('chessApp.resources.images',
                         'wQueen.png'))
    _name = 'queen'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)        

