from tkinter import *
from tkinter import ttk
import shutil
import os

import item65C_func
import item65C_gui



class start(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title("File Transfer")
        self.master.minsize(300,250) #(Height, Width)
        self.master.maxsize(300,250)

##        src_files = ''
##        dest_path = ''
##        count = 0
        
        item65C_gui.load_gui(self)
        

    
        
if __name__ == "__main__":
    root = Tk()
    my_gui = start(root)
    root.mainloop()
