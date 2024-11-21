#Imports the necessary libraries and modules
import tkinter as tk
from tkinter import *
import webbrowser

#Establishes the app, by passing in Frame from tkinter 
class ParentWindow(Frame):
    #initializes a main object of the parent class to base the GUI on
    def __init__(self, master):
        Frame.__init__(self, master)
        #Sets title of GUI window
        self.master.title("Web Page Generator")

        #Creates the label for the custom website text entry field
        self.entry_lbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.entry_lbl.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky=N+W)

        #Creates the entry field for the custom website text 
        self.entry_field = Entry(self.master, width=130, text="")
        self.entry_field.grid(row=1, column=0, columnspan=3, rowspan=1, padx=(10,10), pady=(0,0), sticky=W+S)

        #Creates the button that generates a website with the default text
        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=1, padx=(10,10), pady=(10,10), sticky=E+S)
        #Creates the button that generates a website with the custom text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=2, padx=(10,10), pady=(10,10), sticky=E+S)

    #Creates the function that generates a website with the default text 
    def defaultHTML(self):
        #Establishes the text body for the website
        htmlText = "Stay tuned for our amazing summer sale!"
        #Establishes and opens an index html file to base the website on
        htmlFile = open("index.html", "w")
        #Establishes the HTML code to enter into the index file, including the default text
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #Enters the code into the HTML index file
        htmlFile.write(htmlContent)
        #Closes the HTML index file
        htmlFile.close()
        #Uses the webbrowser module to open the HTML index file, and thus the webpage
        webbrowser.open_new_tab("index.html")

    #Creates the function that generates a website with the default text
    def customHTML(self):
        #Extracts the user input from the entry field and establishes it as the text body for the website
        htmlText = self.entry_field.get()
        #Establishes and opens an index html file to base the website on
        htmlFile = open("index.html", "w")
        #Establishes the HTML code to enter into the index file, including the custom text
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #Enters the code into the HTML index file
        htmlFile.write(htmlContent)
        #Closes the HTML index file
        htmlFile.close()
        #Uses the webbrowser module to open the HTML index file, and thus the webpage
        webbrowser.open_new_tab("index.html")

#Tells the script to run a loop of the app, based on the parentwindow class
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
