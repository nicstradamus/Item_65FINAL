from tkinter import *
from tkinter import ttk
import shutil
import os
from tkinter import filedialog
from tkinter import messagebox

import item65C_main
import item65C_gui



def get_src(src_files,dest_path,count,frame):
    src_files = filedialog.askopenfilenames()
    count = int(0)
    for i in src_files:
        count += 1
    lbl_count = ttk.Label(frame, text= 'Files selected: {}'.format(str(count))).pack()
    print(src_files)
    print(count)

    

def get_dest(src_files,dest_path,count,frame):
    dest_path = filedialog.askdirectory()
    lbl_dest = ttk.Label(frame, text='Destination folder: {}'.format(dest_path)).pack()

    

def move_files(src_files,dest_path,count,frame):
    if count > 1 and len(dest_path) != '':
        shutil.move(src_files,dest_path)
    else:
        messagebox.showinfo(title='Alert', message = 'You must first select files and a destination path.')
        print(count)


if __name__ == "__main__":
    pass
