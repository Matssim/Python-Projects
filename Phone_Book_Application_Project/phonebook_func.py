
import os #Imports OS module to allow for control of programs in the operation system (Windows)
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3 #Imports sqlite3 module to allow for database creation and management

import phonebook_main
import phonebook_gui

#Defines the function that centers the application window on the screen. It passes in (self) to
# assign the listed attributes as part of this class, width(w) and height(h)
def center_window(self, w, h):
    #The master.winfo_() methods are imported from Tkinter to calculate the user's screen size
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #x and y calculates the screen coordinates of the middle of the screen by dividing width and
    # height by 2
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    #The .geometry() method passes in the screen size objects and window size objects w/h/x/y 
    # to format the placement of the window relative to the size of the screen and the window
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

#Defines the function that closes the program when the user clicks the upper corner "X"
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0) #closes all widgets to clear the user's system memory

#===============================================================================================

#Defines the function to create the database 
def create_db(self):
    #Establishes a creates and connects to a daatabase file using the sqlite3 module
    conn = sqlite3.connect('phonebook.db')
    #Defines what to do with the connection open
    with conn:
        #The cursor() method enables the function to make changes in SQL
        cur = conn.cursor()
        #The execute() method uses SQL to create a table in the database. Note that the backslash
        # merely cancels out the line shift so that the code looks tidier in this file.
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        #Commits(saves) table to database 
        conn.commit()
    #Closes the connection
    conn.close()
    #Runs the function defined below to make sure there's an entry in the database
    first_run(self)

#This function creates a dummy entry into the database so that it's never epmty 
def first_run(self):
    data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        #Passes the cursor method into the count_records function, defined below
        cur,count = count_records(cur)
        #if count as established by count-records() is < 1, i.e. empty it enters and commits the
        # dummy entry into the table
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()

#This function counts the contents of tbl_phonebook and passes that number as "count" back to the
# first_run function 
def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count
                          
#This function governs the ListboxSelect event as outlined in the gui file, passed in by the
# "event" argument
def onSelect(self,event):
    #Instanciates whatever triggers the event (widget)
    varList = event.widget
    #This catches the index of the list item that is selected, starting at 0 (first item) as
    # the default
    select = varList.curselection()[0]
    #Passes the index to value 
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        #Selects a tuple of information and equates the tuple index relative to the index of
        # value, i.e. it connects the cells of each column to their related row 
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            #Clears the entry fields and inserts the content of the corresponding index
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

#This is the function that allows the user to add contacts to the database
def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #The strip() method normalizes the data keep formatting consistent in the database
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    #The title() method capitalizes the first letter of name entered
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) #Combines normalized name elements
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!")
    #Controls that the user has not left any empty fields 
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn =sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            #Uses "count" to check database if the entry already exists
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: #Establishes that the data can be added as long as the fullname doesn't already exist
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) #Adds the fullname entry to the listbox
                onClear(self) #Calls the function that clears all the textboxes, as defined below
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) 
        conn.commit()
        conn.close()
    else: 
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

#This defines the function for the delete button
def onDelete(self):
    #Passes the listbox selection index as an argument to identify selction for the function
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        #Makes sure that there is more than one entry in the database before alowing the user to
        #delete an entry
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with ({}) \nwill be permanently deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #Calls the function to clear teh textboxes AND index in the listbox as defined below
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()


def onDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass
#The difference between the below/above functions is that onDeleted also clears the listbox index
def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    
#This function populates the listbox per the current state of the database
def onRefresh(self):
    #Deletes the content of the listbox, so it can be repopulated with the current database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        #Assigning iterations (i) as 0 and incrementing by 1 ensures the following loop only 
        # continues as long as the tuple of entries is longer than the count
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()

def onUpdate(self):
    #This try-except block make sure an entry has been selected before trying to update, otherwise
    # the error messagebox will display
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for \n\nProceed with the update request?".format(var_phone,var_email))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exists in the databade for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email))
            onClear(self)
        conn.close()
    else:
        massagebox.showerror("Missing information","Please select a name from the list \nThen edit the phoneor email information.")
    onClear(self)

if __name__ == "__main__":
    pass





















