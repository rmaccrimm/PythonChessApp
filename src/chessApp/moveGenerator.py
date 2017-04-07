# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from chessApp.chessPieces import *
    
allSpaces = []
for i in range(8):
    for j in range(8):
        allSpaces.append(chr(i+97) + str(j+1))
    
def getPossible(pieceList, piecePos):
    """Get list of possible moves for the piece
    """
    piece = pieceList[piecePos]
    if piece.name == 'pawn':
        return allSpaces
    elif piece.name == 'rook':
        return genRookMoves(pieceList, piecePos)
    elif piece.name == 'knight':
        return allSpaces
    elif piece.name == 'bishop':
        return genBishopMoves(pieceList, piecePos)
    elif piece.name == 'king':
        return allSpaces
    elif piece.name == 'queen':
        return genQueenMoves(pieceList,piecePos)
    else:
        raise ValueError('Piece does not have a valid name')

def getXY(pos):
    """Convert position string to x and y coordinates going from 0 to 7
    """
    if len(pos) == 2:
        x, y = ord(pos[0]) - 97, int(pos[1])-1 
        return x, y
    else:
        raise ValueError('Position string must have two characters')
    
def getPosString(x, y):
    """Convert x and y coordinates to a chess grid notation string
    """
    return chr(x+97) + str(y+1)

def genRookMoves(pieceList, piecePos):
    """Generates possible moves for a rook piece. Will probably be refactored
    at some point.
    """
    possible = []
    piece = pieceList[piecePos]
    color = piece.color
    x, y = getXY(piecePos)
    xInc = x+1
    while(xInc < 8):
        nextPos = getPosString(xInc,y)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        xInc += 1
    xDec = x-1
    while(xDec >= 0):
        nextPos = getPosString(xDec,y)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        xDec -= 1
    yInc = y+1
    while(yInc < 8):
        nextPos = getPosString(x, yInc)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        yInc += 1
    yDec = y-1
    while(yDec >= 0):
        nextPos = getPosString(x, yDec)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        yDec -= 1
    return possible

def genBishopMoves(pieceList, piecePos):
    possible = []
    color = pieceList[piecePos].color
    x, y = getXY(piecePos)
    dx, dy = x+1, y+1
    while(dx < 8 and dy < 8):
        nextPos = getPosString(dx, dy)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        dx += 1
        dy += 1
    dx, dy = x+1, y-1
    while(dx < 8 and dy >= 0):
        nextPos = getPosString(dx, dy)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        dx += 1
        dy -= 1
    dx, dy = x-1, y-1
    while(dx >= 0 and dy >= 0):
        nextPos = getPosString(dx, dy)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        dx -= 1
        dy -= 1
    dx, dy = x-1, y+1
    while(dx >= 0 and dy < 8):
        nextPos = getPosString(dx, dy)
        if nextPos not in pieceList:
            possible.append(nextPos)
        elif pieceList[nextPos].color != color:
            possible.append(nextPos)
            break
        else:
            break
        dx -= 1
        dy += 1
    return possible
        
def genQueenMoves(pieceList, piecePos):
    return (genRookMoves(pieceList, piecePos)
            + genBishopMoves(pieceList, piecePos))
