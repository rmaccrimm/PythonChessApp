# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
from PIL import Image, ImageTk
import inspect


class ChessGui(object):
    """Displays chess board and pieces.
    """
    
    def __init__(self, root, squareSize=60):
        self.root = root
        self.squareSize = squareSize
        self.center = self.squareSize/2
        self.imageSize = 50
        self.listeners = []
        self.images = {}
        self.pieces = {}

        self.frame = Frame(root, bd=5)
        self.board = Canvas(self.frame, height=self.squareSize*8, 
                            width=self.squareSize*8, background='gray')
        self.board.bind('<Button-1>', self.handleClick)
        self.drawBoard()
        self.label = Label(text="Text")
        self.frame.pack(expand=YES)    
        self.board.pack(expand=YES)
        self.label.pack()
            
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
            yPos = self.squareSize*8 - (
                (int(position[1])-1)*self.squareSize + self.squareSize/2)
            self.pieces[position] = self.board.create_image(
                xPos, yPos,image=scaledImage)
            
    def removePiece(self, position):
        """Remove the piece at the given position.
        """
        if self.cellOccupied(position):
            self.board.delete(self.pieces[position])
            del self.images[position]
            del self.pieces[position]
        else:
            raise RuntimeError('No piece to remove')
            
    def clearAll(self):
        """Removes all pieces that have been drawn
        """
        for position in list(self.images):
            self.removePiece(position)
            
    def trackMouse(self, event, piece):
        currPos = self.board.coords(piece)
        self.board.move(piece, event.x-currPos[0], event.y-currPos[1])

    def pickupPiece(self, position):
        """Pick up a piece, causing it to follow the mouse
        """
        self.board.bind('<Motion>', 
            lambda event, piece=self.pieces[position]: 
            self.trackMouse(event, piece))
            
    def handleClick(self, event):
        """Pass name of cell clicked to all listeners. 
        """
        for listener in self.listeners:
            listener.handleClick(event)
            
    def setLabelText(self, text):
        """Set the text on the label below the board
        """
        self.label['text'] = text
    
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
    