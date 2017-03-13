# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from chessApp.chessController import ChessController
from chessApp.chessPieces import Rook

class MockGui(object):
    """Mock gui class used to check function calls made to ChessGui
    """

    def __init__(self, root, size=None):
        self.drawCalled = False
        self.removeCalled = False

    def drawPiece(self, position, image):
        self.drawCalled = True

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
        self.p1, self.pos1 = None, None
        self.p2, self.pos2 = None, None
        self.p3, self.pos3 = None, None
        
    def setUpPieces(self):
        self.p1 = Rook('white')
        self.p2 = Rook('white')
        self.p3 = Rook('black')
        self.pos1 = 'c4'
        self.pos2 = 'd4'
        self.pos3 = 'c5'
        self.controller.addPiece(self.pos1, self.p1)
        self.controller.addPiece(self.pos2, self.p2)
        self.controller.addPiece(self.pos3, self.p3)
        
    def test_setCurrent_InvalidCell(self):
        self.assertRaises(KeyError, self.controller.setCurrent, 'x10')
        
    def test_setCurrent_correctPieceAndCell(self):
        self.p1 = Rook('black')
        position = 'b8'
        self.controller.addPiece(position, self.p1)
        self.controller.setCurrent(position)
        self.assertTrue(self.controller.currentPiece == self.p1 and
                        self.controller.currentCell == position)
                        
    def test_setCurrent_invalidParameter(self):
        self.assertRaises(TypeError, self.controller.setCurrent, 10)
        
    def test_addPiece_callsGuiDraw(self):
        self.controller.addPiece('a1', Rook('white'))
        self.assertTrue(self.mock.drawCalled)
    
    def test_addPiece_notAChessPiece(self):
        self.assertRaises(TypeError, self.controller.addPiece, 'e4', 10)
        
    def test_addPiece_spaceOccupied(self):
        self.controller.addPiece('a1', Rook('white'))
        self.assertRaises(RuntimeError, self.controller.addPiece, 'a1', 
                          Rook('black'))
       
    def test_addPiece_invalidCell(self):
        self.assertRaises(KeyError, self.controller.addPiece, '~9', 
                          Rook('white'))
    
    def test_getPositions_addingPieces(self):
        self.controller.addPiece('a2', Rook('white'))
        self.controller.addPiece('c8', Rook('black'))
        self.controller.addPiece('f6', Rook('black'))
        self.assertEqual(self.controller.getPositions(), ['a2', 'c8', 'f6'])
        
    def test_getPositions_addingAndRemovingPieces(self):
        self.controller.addPiece('a2', Rook('white'))
        self.controller.addPiece('c8', Rook('black'))
        self.controller.addPiece('f6', Rook('black'))
        self.controller.addPiece('g3', Rook('white'))
        self.controller.removePiece('c8')
        self.assertEqual(self.controller.getPositions(), ['a2', 'f6', 'g3'])
        
    def test_getPieces_addingPieces(self):
        self.setUpPieces()
        pieceDict = {self.pos1:self.p1, self.pos2:self.p2, self.pos3:self.p3}
        self.assertEqual(self.controller.getPieces(), pieceDict)
        
    def test_getPieces_addingAndRemovingPieces(self):
        self.setUpPieces()
        self.controller.removePiece(self.pos3)
        pieceDict = {self.pos1:self.p1, self.pos2:self.p2}
        self.assertEqual(self.controller.getPieces(), pieceDict)
       
    def test_removePiece_callsGuiRemove(self):
        self.controller.addPiece('a1', Rook('black'))
        self.controller.removePiece('a1')
        self.assertTrue(self.mock.removeCalled)
       
    def test_removePiece_spaceUnoccupied(self):
        self.assertRaises(RuntimeError, self.controller.removePiece, 'a1')
       
    def test_removePiece_invalidCell(self):
        self.assertRaises(KeyError, self.controller.removePiece, 'f12')
       
    def test_handleClick_emptyCellNoCurrent(self):
        self.controller.handleClick('a1')
        self.assertTrue(self.controller.currentPiece == None and
                        self.controller.currentCell == None)
         
    def test_handleClick_occupiedCellSetsCurrent(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.assertTrue(self.controller.currentPiece == self.p1 and
                        self.controller.currentCell == self.pos1)
        
    def test_handleClick_emptyCellWithCurrentMovesPiece(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.controller.handleClick('c3')
        self.assertTrue(self.controller.chessGrid[self.pos1] == None and
                        self.controller.chessGrid['c3'] == self.p1)
        
    def test_handleClick_emptyCellWithCurrentResetsCurrent(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.controller.handleClick('b4')
        self.assertTrue(self.controller.currentPiece == None and
                        self.controller.currentCell == None)
        
    def test_handleClick_sameColorDoesNothing(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.controller.handleClick(self.pos2)
        self.assertTrue(self.controller.currentPiece == self.p1 and
                        self.controller.currentCell == self.pos1)
        
    def test_handlClick_samePieceResetsCurrent(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.controller.handleClick(self.pos1)
        self.assertTrue(self.controller.currentPiece == None and
                        self.controller.currentCell == None)
        
    def test_handleClick_oppColorMovesPiece(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.controller.handleClick(self.pos3)
        self.assertTrue(self.controller.chessGrid[self.pos3] == self.p1 and
                        self.controller.chessGrid[self.pos1] == None)
    
    def test_handleClick_oppColorResetsCurrent(self):
        self.setUpPieces()
        self.controller.handleClick(self.pos1)
        self.controller.handleClick(self.pos3)
        self.assertTrue(self.controller.currentPiece == None and
                        self.controller.currentCell == None)