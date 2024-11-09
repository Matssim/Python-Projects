#imports the sqlite3 module to enable database management
import sqlite3

#establishes the 'assignment.db' database and opens a connection to it from this script
connection = sqlite3.connect('assignment.db')


with connection:
    #enables the script to edit the database
    editor = connection.cursor()
    #creates the tbl_fileList table in the database and assigns a primary key column
    editor.execute("CREATE TABLE IF NOT EXISTS tbl_fileList(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files STRING)")
    #commits the edit to the database
    connection.commit()
    #closes the connection to the database 
connection.close()

#establishes the list of files to be iterated over and selectively added to the database
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#reestablishes the connection to the 'assignment.db' database 
connection = sqlite3.connect('assignment.db')

#establishes a loop that iterates through the fileList items/files
for files in fileList:
    #creates a conditional statement for files with the .txt file extension
    if files.endswith('.txt'):
        with connection:
            editor = connection.cursor()
            #adds the selected files to the tbl_fileList table
            editor.execute("INSERT INTO tbl_fileList (col_files) VALUES (?)",(files,))
            print(files)
connection.close()
        


