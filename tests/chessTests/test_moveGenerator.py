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
        
    def test_genRookMoves_noPossibleMoves(self):
        posR, posP1, posP2 = 'h1', 'g1', 'h2'
        pieces = {posR:Rook('white'), posP1:Pawn('white'), posP2:Pawn('white')}
        possible = []
        self.assertEqual(genRookMoves(pieces, posR), possible)
        
    def test_genBishopMoves_noBlockingLRBEdges(self):
        pos = 'e3'
        pieces = {pos:Bishop('black')}
        possible = ['f2', 'g1', 'd2', 'c1', 'd4', 'c5', 'b6', 'a7', 'f4', 'g5',
                    'h6']
        self.assertEqual(genBishopMoves(pieces, pos), possible)
        
    def test_genBisihopMoves_topEdgeAndCorners(self):
        pos = 'f6'
        pieces = {pos:Bishop('white')}
        possible = ['g7', 'h8', 'e7', 'd8', 'g5', 'h4', 'e5', 'd4', 'c3', 'b2'
                   'a1']
        self.assertEqual(genBishopMoves(pieces, pos), possible)
        
    def test_genBishopMoves_oppColorBlocking(self):
        posB, posP = 'e3', 'd4'
        pieces = {posB:Bishop('white'), posP:Pawn('white')}
        possible = ['d2', 'c1', 'f2', 'g1', 'f4', 'g5', 'h6']
        self.assertEqual(genBishopMoves(pieces, posB), possible)
        
    def test_genBishopMoves_sameColorBlocking(self):
        posB, posP = 'e7', 'd6'
        pieces = {posB:Bishop('black'), posP:Pawn('white')}
        possible = ['f8', 'd8', 'f6', 'g5', 'h4']
        self.assertEqual(genBishopMoves(pieces, posB), possible)
        
    def test_genRookMoves_noMovesPossible(self):
        posB, posP = 'a8', 'b7'
        pieces = {posB:Bishop('black'), posP:Pawn('black')}
        possible = []
        self.assertEqual(genBishopMoves(pieces, posB), possible)