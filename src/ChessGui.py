# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
from PIL import Image, ImageTk

class ChessGui():
    
    def __init__(self, root):
        self.root = root
        self.chessGrid = {}
        self.chessGrid['a1'] = Canvas(root, width=85, height=85,
                                      background='black')
        self.chessGrid['a1'].grid(row=0, column=0)
        self.chessGrid['a2'] = Canvas(root, width=85, height=85,
                                      background='black')
        self.chessGrid['a2'].grid(row=0, column=1)
        
        blackIcon = Image.open('/home/rmaccrimmon/Pictures/arch start buttons/'
                          + 'start-here monochrome strong.png')
        self.blackImg = ImageTk.PhotoImage(blackIcon)
        
        whiteIcon = Image.open('/home/rmaccrimmon/Pictures/arch start buttons/'
                          + 'start-here monochrome light.png')
        self.whiteImg = ImageTk.PhotoImage(whiteIcon)
        
        #self.chessGrid['a1'].create_image(40, 40, image=self.blackImg)
        self.chessGrid['a2'].create_image(42.5, 42.5, image=self.whiteImg)
        
        self.position = 'a2'

    def swap(self):
        self.chessGrid[self.position].delete('all')
        
        if self.position == 'a1':
            self.position = 'a2'
        elif self.position == 'a2':
            self.position = 'a1'
        
        self.chessGrid[self.position].create_image(42.5, 42.5, 
                                                   image=self.whiteImg)
