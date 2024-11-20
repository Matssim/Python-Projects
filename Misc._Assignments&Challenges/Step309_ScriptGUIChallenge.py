import os
from tkinter import *
import tkinter as tk


class window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("Check files")

        load_gui(self)

def load_gui(self):
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text="Browse...")
    self.btn_browse1.grid(row=0,column=0,padx=(20,20),pady=(20,5),sticky=N+E+W+S)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text="Browse...")
    self.btn_browse2.grid(row=1,column=0,padx=(20,20),pady=(5,5),sticky=N+E+W+S)
    self.btn_filecheck = tk.Button(self.master,width=12,height=2,text="Check for files...")
    self.btn_filecheck.grid(row=2,column=0,padx=(20,20),pady=(5,20),sticky=N+E+W+S)
    self.btn_close = tk.Button(self.master,width=12,height=2,text="Close Program")
    self.btn_close.grid(row=2,column=4,padx=(20,20),pady=(5,20),sticky=N+E+W+S)

    self.txt_entry1 = tk.Entry(self.master,width=48,text='')
    self.txt_entry1.grid(row=0,column=1,rowspan=1,columnspan=4,padx=(10,20),pady=(20,5),sticky=N+E+W+S)
    self.txt_entry2 = tk.Entry(self.master,width=48,text='')
    self.txt_entry2.grid(row=1,column=1,rowspan=1,columnspan=4,padx=(10,20),pady=(5,5),sticky=N+E+W+S)


if __name__ == "__main__":
    root = tk.Tk()
    Gui = window(root)
