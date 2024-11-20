# Python Version:   3.13.3
#
# Author:           Daniel A. Christie
#                   (Reproduced and edited by Mats B. Simonsen)
#
# Purpose:          Phonebook app demo. An exercise in using OOP, Tkinter GUI module,
#                   using Tkinter Parent-Child relationships
#
# Tested OS:        Written for Windows 10, tested on Windows 11.

#Imports all contents of Tkinter and assigns it as "tk" for the purposes of this script
from tkinter import * 
import tkinter as tk
from tkinter import messagebox

#Imports modules from external project files
import phonebook_gui
import phonebook_func

# Defines the class that inherits the attributes of the "Frame" class in Tkinter
class ParentWindow(Frame):
    #Initializes the objects fo the class, including itself, the "master" Frame configuration from
    # tkinter, undefined arguments (*args) and undefined keyword arguments (**kwargs)
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Defines the master frame configuration. master is invoked from tkinter's Frame module
        self.master = master
        self.master.minsize(500,300) #(Height, Width) - Locks in window size
        self.master.maxsize(500,300)
        # The .center_window() method will center appp on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo") #Sets a title
        self.master.configure(bg="#F0F0F0") #Sets a background color
        # The .protocol() method will catch if a users clicks the upper corner "X" to close the window
        # and runs the Windows protocol to ask if the user would like to close it
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Loads in the GUI widgets from the module in a separate file
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk() #Creates the window
    App = ParentWindow(root) #Calls App kw so Tkinter can open the window
    root.mainloop() #Keeps the program running until loop is closed
