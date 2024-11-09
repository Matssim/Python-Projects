import os


def writeData():
    data = "\nHello, world!"
    with open('test.txt', 'a') as f: #'a' opens the file for writing, appending to the end of the file
        f.write(data)
        f.close()
    


def openFile():
    with open('test.txt', 'r') as f: #creates a with/while loop that runs as long as the file is being opened for reading and assignis it a variable value of f 
        data =  f.read() #declares data as the file being opened for reading and read by the .read method 
        print(data) #prints what was being read
        f.close() #tells the file to close, to prevent memory leaks


if __name__ == "__main__":
    writeData()
    openFile()
