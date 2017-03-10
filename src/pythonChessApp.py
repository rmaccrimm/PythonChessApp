# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import Tk
from tkinter import ttk
from ChessGui import *
from ChessController import *

class obs():
    def __init__(self):
        pass
    
    def notify(self, string):
        print(string)
        
if __name__ == "__main__":
    root = Tk()
    root.title('Chess')
    frame = Frame(root)
    gui = ChessGui(frame)
    controller = ChessController(gui)

    image = Image.open('resources/bPawn.png')
    for i in range(8):
        gui.drawPiece('b'+str(1+i), image)

    frame.pack()

    root.mainloop()
