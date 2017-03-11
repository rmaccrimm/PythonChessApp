# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import Tk
from tkinter import ttk
from ChessGui import *
from ChessController import *
from ChessPiece import *

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
    controller.initPieces()
    frame.pack()
    root.mainloop()
