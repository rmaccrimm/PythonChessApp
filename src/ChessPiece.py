# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from PIL import Image

class ChessPiece():
    
    def movePossible(position):
        return True

class BlackPawn(ChessPiece):
    image = Image.open('resources/bPawn.png')
    name = 'Black Pawn'
  
class WhitePawn(ChessPiece):
    image = Image.open('resources/wPawn.png')
    name = 'White Pawn'
    
class BlackKnight(ChessPiece):
    image = Image.open('resources/bKnight.png')
    name = 'Black Knight'
    
class WhiteKnight(ChessPiece):
    image = Image.open('resources/wKnight.png')
    name = 'White Knight'
    
class BlackKing(ChessPiece):
    image = Image.open('resources/bKing.png')
    name = 'Black King'
    
class WhiteKing(ChessPiece):
    image = Image.open('resources/wKing.png')
    name = 'White King'

class BlackQueen(ChessPiece):
    image = Image.open('resources/bQueen.png')
    name = 'Black Queen'

class WhiteQueen(ChessPiece):
    image = Image.open('resources/wQueen.png')
    name = 'White Queen'
    
class BlackRook(ChessPiece):
    image = Image.open('resources/bRook.png')
    name = 'Black Rook'
    
class WhiteRook(ChessPiece):
    image = Image.open('resources/wRook.png')
    name = 'White Rook'
    
class BlackBishop(ChessPiece):
    image = Image.open('resources/bBishop.png')
    name = 'Black Rook'
    
class WhiteBishop(ChessPiece):
    image = Image.open('resources/wBishop.png')
    name = 'White Bishop'
