# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from PIL import Image


class ChessPiece():
    """Stores an image and name for each type of chess piece. Later on will 
    handle move generation to check if moves are valid.
    """
    
    def __init__(self, color):
        self.color = color.lower()
        if self.color == 'black':
            self.image = self.bImage
        elif self.color == 'white':
            self.image = self.wImage
        else:
            raise ValueError('Invalid piece color')
    
    def movePossible(position):
        """Check if move is valid for the piece. To be implemented in the 
        future.
        """
        return True


class Pawn(ChessPiece):
    bImage = Image.open('resources/bPawn.png')
    wImage = Image.open('resources/wPawn.png')
    name = 'pawn'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)


class Knight(ChessPiece):
    bImage = Image.open('resources/bKnight.png')
    wImage = Image.open('resources/wKnight.png')
    name = 'knight'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)
  
        
class Rook(ChessPiece):
    bImage = Image.open('resources/bRook.png')
    wImage = Image.open('resources/wRook.png')
    name = 'rook'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)
  
        
class Bishop(ChessPiece):
    bImage = Image.open('resources/bBishop.png')
    wImage = Image.open('resources/wBishop.png')
    name = 'bishop'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)
 
        
class King(ChessPiece):
    bImage = Image.open('resources/bKing.png')
    wImage = Image.open('resources/wKing.png')
    name = 'king'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)        
  
        
class Queen(ChessPiece):
    bImage = Image.open('resources/bQueen.png')
    wImage = Image.open('resources/wQueen.png')
    name = 'queen'
    
    def __init__(self, color='black'):
        ChessPiece.__init__(self, color)        

