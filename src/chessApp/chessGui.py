# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
import itertools
from PIL import Image, ImageTk
import inspect


class ChessGui(object):
    """Displays chess board and pieces.
    """
    
    def __init__(self, root, squareSize=60):
        self.board = {}
        self.root = root
        self.squareSize = squareSize
        self.center = self.squareSize/2
        self.imageSize = 50
        self.listeners = []
        self.images = {}

        self.frame = Frame(root, bd=5)
        self.board = Canvas(self.frame, height=self.squareSize*8, 
                            width=self.squareSize*8, background='gray')
        self.drawBoard()
        self.label = Label(text="Text")
        self.frame.pack(expand=YES)    
        self.board.pack(expand=YES)
        self.label.pack()
        """for i in range(8):
            for j in range(8):
                key = chr(i+97) + str(j+1)
                self.board[key] = Canvas(root, width = self.squareSize, 
                    height=self.squareSize, background=next(colorIter))
                self.board[key].grid(row=8-j, column=i)
                self.board[key].bind('<Button-1>', 
                    lambda event, position=key: 
                    self.handleClick(event, position))
            next(colorIter)"""
            
    def drawBoard(self):
        for i in range(4):
            for j in range(4):
                x1 = self.squareSize*2*i
                y1 = self.squareSize*2*j
                x2 = x1 + self.squareSize
                y2 = y1 + self.squareSize
                self.board.create_rectangle(x1, y1, x2, y2, fill='white')
                x1 += self.squareSize
                x2 += self.squareSize
                self.board.create_rectangle(x1, y1, x2, y2, fill='gray')
                y1 += self.squareSize
                y2 += self.squareSize
                self.board.create_rectangle(x1, y1, x2, y2, fill='white')
                x1 -= self.squareSize
                x2 -= self.squareSize
                self.board.create_rectangle(x1, y1, x2, y2, fill='gray')
        boardSize = self.squareSize*8
        self.board.create_line(0, 1, boardSize, 1)
        self.board.create_line(1, 0, 1, boardSize)
                
    def cellOccupied(self, position):
        """Check if an image has already been drawn at the given position
        """
        if position in self.images:
            return True
        else:
            return False
            
    def drawPiece(self, position, image):
        """Draw the image at the given grid position, specified by chess
        algebraic notation.
        """
        if self.cellOccupied(position):
            raise RuntimeError('Cell already occupied')
        else:
            scaledImage = ImageTk.PhotoImage(image.resize(
                (self.imageSize, self.imageSize), Image.ANTIALIAS))
            self.images[position] = scaledImage
            xPos = (ord(position[0]) - 97)*self.squareSize + self.squareSize/2
            yPos = (int(position[1])-1)*self.squareSize + self.squareSize/2
            print(str(xPos) + ' '  + str(yPos))
            self.board.create_image(xPos, yPos,image=scaledImage)
            
    def removePiece(self, position):
        """Remove the piece at the given position.
        """
        if self.cellOccupied(position):
            self.board[position].delete('all')
            del self.images[position]
        else:
            raise RuntimeError('No piece to remove')
            
    def clearAll(self):
        """Removes all pieces that have been drawn
        """
        for position in list(self.images):
            self.removePiece(position)
            
    def handleClick(self, event, position):
        """Pass the name of the cell clicked to all listeners. 
        """
        for listener in self.listeners:
            listener.handleClick(position)
    
    def addListener(self, listener):
        """Register a listener to recieve input when a cell is clicked. 
        """
        handleClick = getattr(listener, 'handleClick', None)
        if callable(handleClick):
            params = inspect.getfullargspec(listener.handleClick).args
            if(len(params) != 2):
                raise RuntimeError('Listener notify method must have only 2'
                                   +'parameters')
            else:
                self.listeners.append(listener)
        else:
            raise RuntimeError('Listener has no method called notify')
    