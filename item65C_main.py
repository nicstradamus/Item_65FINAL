from tkinter import *
from tkinter import ttk
import shutil
import os
from tkinter import filedialog
from tkinter import messagebox

import item65C_gui
import item65C_func 

class start(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title("File Transfer")

        item65C_gui.load_gui(self)
        

    
        

root = Tk()
my_gui = start(root)
root.mainloop()
