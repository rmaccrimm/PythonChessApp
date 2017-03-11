# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
import itertools
from PIL import Image, ImageTk

class ChessGui():
    
    def __init__(self, root, squareSize=60):
        self.board = {}
        self.root = root
        self.squareSize = 60
        self.center = squareSize/2
        self.imageSize = 50
        self.listeners = []
        self.images = {}
        colorIter = itertools.cycle(['grey', 'white'])

        for i in range(8):
            for j in range(8):
                key = chr(i+97) + str(j+1)
                self.board[key] = Canvas(root, width = self.squareSize, 
                    height=self.squareSize, background=next(colorIter))
                self.board[key].grid(row=8-j, column=i)
                self.board[key].bind('<Button-1>', 
                    lambda event, position=key: self.notify(event, position))
            next(colorIter)
            
    def drawPiece(self, position, image):
        try:
            if self.board[position].find_all():
                raise RuntimeError('Cell already occupied')
            else:
                scaledImage = ImageTk.PhotoImage(image.resize(
                    (self.imageSize, self.imageSize), Image.ANTIALIAS))
                self.images[position] = scaledImage
                self.board[position].create_image(self.center, self.center,
                    image=scaledImage)
        except KeyError:
            print('Tried to draw in non-existent cell')
    
    def removePiece(self, position):
        try:
            if self.board[position].find_all():
                self.board[position].delete('all')
                del self.images[position]
        except KeyError:
            print('No Piece to remove')
            
    def notify(self, event, position):
        for listener in self.listeners:
            try:
                listener.notify(position)
            except: 
                pass
    
    def addListener(self, listener):
        self.listeners.append(listener)
    