import os
import time

fPath = 'C:\\Users\\matss\\Documents\\myRepository\\Python-Projects\\Misc._Assignments&Challenges\\Step_209FileIOTutorial\\'

fList = os.listdir(path=fPath)

fExt = ('.txt')

fModTime = os.path.getmtime(fPath)
fLocModTime = time.ctime(fModTime)

for files in fList:
    if files.endswith(fExt):
        fname = os.path.join(fPath, files)
        print(fname, fLocModTime)









