# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tkinter import Tk
from ChessGui import *
    
if __name__ == "__main__":
    root = Tk()
    gui = ChessGui(root)
    root.mainloop()
