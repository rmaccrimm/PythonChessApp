# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from PIL import Image
from tkinter import Tk
from chessApp.chessGui import ChessGui
from pkg_resources import resource_filename

class  ChessGui_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.root = Tk()
        self.gui = ChessGui(self.root)
        self.image = Image.open(resource_filename('chessApp.resources.images',
                                'bPawn.png'))
        
    def tearDown(self):
        self.gui.clearAll()
        
    def test_drawPieceCellOccupied(self):
        position = 'a1'
        self.gui.drawPiece(position, self.image)
        self.assertRaises(RuntimeError, self.gui.drawPiece, position, 
                          self.image)
                          
    def test_drawPieceInvalidCell(self):
        position = 'a9'
        self.assertRaises(KeyError, self.gui.drawPiece, position, self.image)
        
    def test_drawPieceCorrectNumberOfImages(self):
        self.gui.drawPiece('a1', self.image)
        self.gui.drawPiece('a2', self.image)
        self.assertEqual(len(self.gui.images), 2)
        
    def test_clearAll(self):
        self.gui.drawPiece('a1', self.image)
        self.gui.drawPiece('a2', self.image)
        self.gui.clearAll()
        self.assertEqual(len(self.gui.images), 0)
        
    def test_removeNoPiece(self):
        self.assertRaises(RuntimeError, self.gui.removePiece, 'a1')
    
    def test_removeCorrectNumberOfImages(self):
        self.gui.drawPiece('a1', self.image)
        self.gui.drawPiece('a2', self.image)
        self.gui.removePiece('a1')
        self.assertEqual(len(self.gui.images), 1)
        
    def test_cellOccupiedNoDraw(self):
        self.assertFalse(self.gui.cellOccupied('h3'))
    
    def test_cellOccupiedAfterDraw(self):
        self.gui.drawPiece('g8', self.image)
        self.assertTrue(self.gui.cellOccupied('g8'))
    
    def test_cellOccupiedInvalidCell(self):
        self.assertRaises(KeyError, self.gui.cellOccupied, 'f0')
    
    def test_cellOccupiedAfterRemove(self):
        self.gui.drawPiece('e6', self.image)
        self.gui.removePiece('e6')
        self.assertFalse(self.gui.cellOccupied('e6'))
        
    def test_addListenerNoHandleClickAttribute(self):
        listener = 10
        self.assertRaises(RuntimeError, self.gui.addListener, listener)
        
    def test_addListenerHandleClickNotMethod(self):
        class tempClass(object):
            def __init__(self):
                self.handleClick = None
        listener = tempClass()
        self.assertRaises(RuntimeError, self.gui.addListener, listener)
        
    def test_addListenerWrongArguments(self):
        class tempClass(object):
            def handleClick(self):
                pass
        listener = tempClass()
        self.assertRaises(RuntimeError, self.gui.addListener, listener)
        
    def test_handleClick(self):
        class tempClass(object):
            def __init__(self):
                self.notified = False
            def handleClick(self, arg):
                self.notified = True
        listener = tempClass()
        self.gui.addListener(listener)
        self.gui.handleClick('event', 'arg')
        self.assertTrue(listener.notified)
        
        
