
from tkinter import *
from tkinter import ttk
##import shutil
##import os
##from tkinter import filedialog
##from tkinter import messagebox

import item65C_func
import item65C_gui



class start(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title("File Transfer")
        self.master.minsize(300,180) #(Height, Width)
        self.master.maxsize(300,180)

##        src_files = ''
##        dest_path = ''
##        count = 0
        
        item65C_gui.load_gui(self)
        

    
        

root = Tk()
my_gui = start(root)
root.mainloop()
