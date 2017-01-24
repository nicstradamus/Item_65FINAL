from tkinter import *
from tkinter import ttk
import shutil
import os

import item65C_func 
import item65C_main


def load_gui(self):
    
    #Add button
    self.btn_src = ttk.Button(self.master,text = 'Select Files',
                                    command = lambda: item65C_func.get_src(count)).pack(pady = (10,10))
    self.btn_dest = ttk.Button(self.master,text = 'Select Destination',
                                    command = lambda: item65C_func.get_dest(dest_path)).pack(pady = (10,10))
    self.btn_move = ttk.Button(self.master,text = 'Move Files',
                                    command = lambda: item65C_func.move_files(src_files,dest_path,count)).pack(pady = (10,10))

    #Label variables
    src_files = '???'
    count = '???'
    dest_path = '???'

    #Add labels with variable output
    lbl_count = ttk.Label(self.master, text= 'Files selected: {}'.format(str(count))).pack()
    lbl_dest = ttk.Label(self.master, text='Destination folder: {}'.format(dest_path)).pack()

if __name__ == "__main__":
    pass
