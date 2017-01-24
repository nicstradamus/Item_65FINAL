from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
import time

import item65C_main
import item65C_gui



def get_src(self):
    self.source_dir = filedialog.askdirectory()
    self.source_files = (os.listdir(self.source_dir))
    self.source.set(self.source_dir)
    

    
def get_dest(self):
    self.destination_dir = filedialog.askdirectory()
    self.destination.set(self.destination_dir)
    

def move_files(self):
    self.time_now     = time.time()
    self.day          = 86400
    self.count        = False
    
    if (self.source) == '???' and (self.destination) == '???':
        messagebox.showinfo(title='Alert', message = 'You must first select files and a destination path.')
    elif (self.source_dir) == (self.destination_dir):
        messagebox.showinfo(title='Alert', message = 'Source and Destination paths cannot be the same.')

    else:
        for i in self.source_files:
            self.source_path = (os.path.join(self.source_dir,i))
            self.diff_mod    = self.time_now - (os.path.getmtime(self.source_path))
            self.diff_create = self.time_now - (os.path.getctime(self.source_path))

            if (self.diff_mod < self.day) or (self.diff_create < self.day):
                shutil.move((os.path.join(self.source_dir,i)),self.destination_dir)
                self.count = True
    if self.count == True:
        messagebox.showinfo(title='Success', message = "Files transferred successfully!")
    else:
        messagebox.showinfo(title='Success', message = "No files meet transfer criteria.")




if __name__ == "__main__":
    pass
