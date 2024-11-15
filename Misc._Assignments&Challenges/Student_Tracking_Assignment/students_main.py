
from tkinter import *
import tkinter as tk

import students_gui
import students_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(500,300) 
        self.master.maxsize(500,400)
        students_func.center_window(self,500,400)
        self.master.title("Student Tracking") 
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: students_func.ask_quit(self))
        arg = self.master

        students_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk() 
    App = ParentWindow(root) 
    root.mainloop()










