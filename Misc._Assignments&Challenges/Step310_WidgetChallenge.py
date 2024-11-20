import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk

class window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("Select directory")

        load_gui(self)

##################################################################################################################
        
def load_gui(self):
    self.btn_browse = tk.Button(self.master,width=12,height=1,text="Browse...",command=lambda: browse(self))
    self.btn_browse.grid(row=0,column=0,padx=(20,20),pady=(20,5),sticky=N+E+W+S)
    self.btn_filecheck = tk.Button(self.master,width=12,height=2,text="Check for files...")
    self.btn_filecheck.grid(row=2,column=0,padx=(20,20),pady=(5,20),sticky=N+E+W+S)
    self.btn_close = tk.Button(self.master,width=12,height=2,text="Close Program",command=lambda: close(self))
    self.btn_close.grid(row=2,column=4,padx=(20,20),pady=(5,20),sticky=N+E+W+S)

    self.txt_directory = tk.Text(self.master,width=48,height=2)
    self.txt_directory.grid(row=0,column=1,rowspan=1,columnspan=4,padx=(10,20),pady=(20,5),sticky=N+E+W+S)

##################################################################################################################
    
def close(self):
    self.master.destroy()
    os._exit(0)

def browse(self):
    selected_directory = tk.filedialog.askdirectory()
    self.txt_directory.insert(END, selected_directory)

##################################################################################################################

if __name__ == "__main__":
    root = tk.Tk()
    Gui = window(root)
