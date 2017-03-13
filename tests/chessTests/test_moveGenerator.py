# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from chessApp.moveGenerator import *


class  MoveGenerator_TestCase(unittest.TestCase):
    """Test for move generation. Sets up a various scenarious and checks that 
    expected moves are allowed or not
    """
    
    def test_getXY_min(self):
        x, y = getXY('a1')
        self.assertTrue((x,y) == (0,0))
        
    def test_getXY_max(self):
        x, y = getXY('h8')
        self.assertTrue((x,y) == (7,7))
        
    def test_getPosString_normalInput(self):
        self.assertEqual(getPosString(3,4), 'd5')
        
    def test_getPosString_min(self):
        self.assertEqual(getPosString(0,0), 'a1')
        
    def test_getPosString_max(self):
        self.assertEqual(getPosString(7,7), 'h8')
        
    def test_genRookMoves_noPiecesBlocking(self):
        pos = 'e4'
        pieces = {pos:Rook()}
        possible = ['e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8', 'a4', 'b4', 'c4',
                    'd4', 'f4', 'g4']
        self.assertTrue(genRookMoves(pieces, pos), possible)
        
    def test_genRookMoves_oppColorBlocking(self):
        posR, posP = 'e4', 'e5'
        pieces = {posR:Rook('white'), posP:Pawn('black')}
        possible = ['e1', 'e2', 'e3', 'e5', 'a4', 'b4', 'c4', 'd4', 'f4', 'g4']
        self.assertTrue(genRookMoves(pieces, posR), possible)
        
    def test_genRookMoves_sameColorBlocking(self):
        posR, posP = 'e4', 'e5'
        pieces = {posR:Rook('white'), posP:Pawn('white')}
        possible = ['e1', 'e2', 'e3', 'a4', 'b4', 'c4', 'd4', 'f4', 'g4']
        self.assertTrue(genRookMoves(pieces, posR), possible)