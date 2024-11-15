import tkinter
from tkinter import * #imports all widgets of Tkinter


#Creates a child class of the Frame class, imported from Tkinter
class ParentWindow(Frame): 
    def __init__ (self, master): #Initializes the "master" object(assigns it's values before it is created)
        Frame.__init__(self) #initializes the master object as an instance of Frame

        self.master = master #passes "master" into the "self.master" container
        self.master.resizable(width=False, height=False) #Removes user's availability to resize window
        self.master.geometry('{}x{}'.format(700, 400)) #Sets the window size by pixels
        self.master.title('Learning Tkinter!') #Sets the program title
        self.master.config(bg='lightgray') #sets a background color

        self.varFName = StringVar() #Instaciates StringVar (stringvariable) from Tkinter and passes it to varFName
        self.varLName = StringVar()

# The following code could be used to directly assign and display values |-->
#       self.varFName.set('Bob') #assigns a value to the variable
#       self.varLName.set('Smith')  
#
#       print(self.varFName.get()) #Uses the .get() method to retrieve the value
#       print(self.varLName.get()) <--|

        #Assigns a label to the entry fields coded below, using the gid to place them in the window
        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        #Assigns a display field that will be called by the submit function to display the user input
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
        
        #Assigns an entry field to the program, gives it a name and passing in variables and formating
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        #calls the Tkinter .grid() method to display the entry (alternatively you could use the .pack() method)
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0)) 

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)
        #padx = horizontal padding, pady = vertical padding, numbers in paranthesis are right,left
        #sticky = sticky posistion, NE = North/East (i.e. horizontal/veritcal)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    #Defines the function that is activated by clicking the submit button, retrives the input from the entry fields
    # vie the .get() method and assigns it to the fn'ln variables
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        #chnanges the lblDisplay field using the .config() method to call the inputs and display them in a string
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        
    #Defines the function that is activated by clicking the cancel button, closes the master (window)
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk() #Calls on the Tkinter class and passes it to "root"
    App = ParentWindow(root) #Instanciates the ParentWindow class, with the TKinter (Tk) class instanciated and passes it to "App"
    root.mainloop()#Keeps the program running until loop is closed
    
