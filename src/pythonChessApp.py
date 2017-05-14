# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import Tk
from chessApp.chessGui import *
from chessApp.chessController import *
from chessApp.chessPieces import *
        
if __name__ == "__main__":
    root = Tk()
    root.title('Chess')
    #frame = Frame(root)
    gui = ChessGui(root)
    controller = ChessController(gui)
    controller.initPieces()
    root.mainloop()
