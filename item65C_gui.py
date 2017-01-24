from tkinter import *
from tkinter import ttk
import shutil
import os

import item65C_func 
import item65C_main


def load_gui(self):

    self.source = StringVar()
    self.source.set("???")
    self.source_dir = ''
    self.destination_dir = ''
    self.destination = StringVar()
    self.destination.set("???")

    
    #SELECT SOURCE button
    self.btn_src = ttk.Button(self.master,text = 'Select Source',
                                    command = lambda: item65C_func.get_src(self)).pack(pady = (30,0))
    #SELECT SOURCE labels
    self.lbl_srch  = ttk.Label(self.master, text = 'Source folder:').pack(pady=(10,0))
    self.lbl_src  = ttk.Label(self.master, textvariable = self.source).pack()
    
    #SELECT DESTINATION button
    self.btn_dest = ttk.Button(self.master,text = 'Select Destination',
                                    command = lambda: item65C_func.get_dest(self)).pack(pady = (10,10))
    #SELECT DESTINATION labels
    self.lbl_desth  = ttk.Label(self.master, text = 'Destination folder:').pack()
    self.lbl_dest = ttk.Label(self.master, textvariable = self.destination).pack()

    #MOVE FILES button
    self.btn_move = ttk.Button(self.master,text = 'Move Files',
                                    command = lambda: item65C_func.move_files(self)).pack(pady = (20,10))

    
if __name__ == "__main__":
    pass
