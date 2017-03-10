# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from ChessPiece import *
from tkinter import *
from PIL import Image, ImageTk
import itertools

class ChessCell():
    
    def __init__(self, parent, row=0, column=0, size=60, color='black'):
        self.parent = parent
        self.size = size
        self.canvas = Canvas(parent, width = self.size, height=self.size,
                             background=color)
        self.canvas.grid(row=row, column=column)
        self.active = False
        self.image = Image.open('resources/bPawn.png')
        self.scaledImage = ImageTk.PhotoImage(
            self.image.resize((50,50), Image.ANTIALIAS))
        
    def handleClick(self, event):
        if self.active:
            pass
        
    def add(self):
        self.canvas.create_image(self.size/2, self.size/2, 
                                 image=self.scaledImage)
    
    def remove(self):
        pass
