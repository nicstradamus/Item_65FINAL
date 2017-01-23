from tkinter import *
import tkinter as ttk

import item65C_func 
import item65C_main


def load_gui(self):
    
    #Init vars
    src_files = ''
    dest_path = ''
    count = 0
    
    #Add button
    self.btn_src = ttk.Button(self.master,text = 'Select Files',
                                    command = lambda: item65C_func.get_src(src_files,dest_path,count)).pack(pady = (10,10))
    self.btn_dest = ttk.Button(self.master,text = 'Select Destination',
                                    command = lambda: item65C_func.get_dest(src_files,dest_path,count)).pack(pady = (10,10))
    self.btn_move = ttk.Button(self.master,text = 'Move Files',
                                    command = lambda: item65C_func.move_files(src_files,dest_path,count)).pack(pady = (10,10))


if __name__ == "__main__":
    pass
