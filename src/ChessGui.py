# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
from PIL import Image, ImageTk
import itertools

class ChessGui():
    
    def __init__(self, root):
        self.chessGrid = {}
        self.root = root
        self.squareLength = 60
        colorIter = itertools.cycle(['black', 'white'])
        
        for i in range(8):
            for j in range(8):
                key = chr(i+97) + str(j+1)
                self.chessGrid[key] = Canvas(self.root, width=self.squareLength,
                    height=self.squareLength, background=next(colorIter))
                self.chessGrid[key].grid(row=8-i, column=j)
            next(colorIter)
        keys = []
        for key in self.chessGrid:
            keys.append(key)
        self.keys = itertools.cycle(keys)
        self.image = Image.open('resources/bPawn.png')                        
        self.scaledImage = ImageTk.PhotoImage(
            self.image.resize((50,50), Image.ANTIALIAS))
        self.chessGrid['a1'].create_image(self.squareLength/2, 
            self.squareLength/2, image=self.scaledImage)
        self.position = next(self.keys)
        
        self.chessGrid['a1'].bind('<Button-1>', self.moveNext)

    def moveNext(self, event):
        self.chessGrid[self.position].delete('all')
        self.position = next(self.keys)
        
        self.chessGrid[self.position].create_image(self.squareLength/2, 
            self.squareLength/2, image=self.scaledImage)
