# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from PIL import Image
from chessApp.chessPieces import ChessPiece, Pawn


class  ChessPiece_TestCase(unittest.TestCase):
    """Class for testing just the chess piece base class methods
    """
        
    def test_initCapitalColor(self):
        piece = Pawn('BlaCK')
        self.assertEqual(piece.color, 'black')
        
    def test_initInvalidColor(self):
        self.assertRaises(ValueError, Pawn, 'arg')
