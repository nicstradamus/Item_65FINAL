from tkinter import *
import tkinter as ttk

import item65C_main
import item65C_func

def load_gui(self):
    frame = ttk.LabelFrame(master, text = 'File Transfer')
    frame.pack()
    #Config
    frame.config(height = 200, width = 300)
    frame.config(relief = GROOVE)

    #Add button
    btn_src        = ttk.Button(frame,text = 'Select Files',
                                    command = lambda: get_src(src_files,dest_path,count,frame)).pack(pady = (10,10))
    btn_dest       = ttk.Button(frame,text = 'Select Destination',
                                    command = lambda: get_dest(src_files,dest_path,count,frame)).pack(pady = (10,10))
    btn_move       = ttk.Button(frame,text = 'Move Files',
                                    command = lambda: move_files(src_files,dest_path,count,frame)).pack(pady = (10,10))
    #Padding
    frame.config(padding = (50,15))

if __name__ == "__main__":
    pass
