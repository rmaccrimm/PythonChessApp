# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from chessApp.chessController import ChessController

class MockGui(object):
    """Mock gui class used to check function calls made to ChessGui
    """

    def __init__(self, root, size=None):
        self.addCalled = False
        self.removeCalled = False

    def addPiece(self, position, image):
        self.addCalled = True

    def removePiece(self, position):
        self.removeCalled = True
        
    def addListener(self, listener):
        pass
        
class  ChessController_TestCase(unittest.TestCase):
    """Test cases for the chess controller. All moves checked are valid moves
    to avoid issues when move checking is implemented later
    """
    
    def setUp(self):
        self.mock = MockGui(None)
        self.controller = ChessController(self.mock)
        self.controller.addPiece('c3', Rook('white'))
        self.controller.addPiece('d3', Rook('white'))
        self.controller.addPiece('c4', Rook('black'))
        self.controller.addPiece('d4', Rook('black'))
        
    def test_setCurrent_InvalidCell(self):
        pass
    
    def test_addPiece_callsGuiDraw(self):
        pass
    
    def test_addPiece_correctNumberOfPieces(self):
        pass
    
    def test_addPiece_spaceOccupied(self):
        pass
    
    def test_addPiece_invalidCell(self):
        pass
    
    def test_removePiece_callsGuiRemove(self):
        pass
    
    def test_removePiece_correctNumberOfPieces(self):
        pass
    
    def test_removePiece_spaceUnoccupied(self):
        pass
    
    def test_removePiece_invalidCell(self):
        pass
    
    def test_handleClick_emptyCellNoCurrent(self):
        pass
    
    def test_handleClick_occupiedCellSetsCurrent(self):
        pass
    
    def test_handleClick_emptyCellRemovesExisting(self):
        pass
    
    def test_handleClick_emptyCellAddsNew(self):
        pass
    
    def test_handleClick_sameColorResetsCurrent(self):
        pass
    
    def test_handlClick_samePieceResetsCurrent(self):
        pass
    
    def test_handleClick_oppColorRemovesOpposite(self):
        pass
    
    def test_handleClick_oppColorRemovesCurrent(self):
        pass
    
    def test_handleClick_oppColorAddsNew(self):
        pass
    
    def test_handleClick_oppColorResetsCurrent(self):
        pass