from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os

import item65C_main
import item65C_gui



def get_src(count):
    src_files = filedialog.askopenfilenames()
    count = int(0)
    for i in src_files:
        count += 1
    return src_files,count

    
def get_dest(dest_path):
    dest_path = filedialog.askdirectory()
    return dest_path

    

def move_files(src_files,dest_path,count):
    print(count)
    print(src_files)
    print(dest_path)
    if (count) > 1 and (dest_path) != '???':
        shutil.move(src_files,dest_path)
    else:
        messagebox.showinfo(title='Alert', message = 'You must first select files and a destination path.')
        print(count)


if __name__ == "__main__":
    pass
