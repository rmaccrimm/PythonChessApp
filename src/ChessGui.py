# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChessGui():
    
    def __init__(self, root):
        self.canvas = Canvas(root, width=200, height=100, background='white')

        icon = Image.open('/home/rmaccrimmon/Pictures/arch start buttons/'
                          + 'start-here lp blue.png')
        self.image = ImageTk.PhotoImage(icon)
        canvasImg = self.canvas.create_image(50, 50, image=self.image)
        self.canvas.pack()
