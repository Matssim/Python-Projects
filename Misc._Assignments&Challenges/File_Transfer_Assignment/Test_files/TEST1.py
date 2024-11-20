import os
import shutil
import time
from datetime import timedelta, datetime
from pathlib import Path

cwd_path = Path.cwd()
source_path = os.path.join(cwd_path, "Customer Source")
destination_path = os.path.join(cwd_path, "Customer Destination")
sourcefolder_file = os.listdir(source_path)
for i in sourcefolder_file:
    sourcefile_path = os.path.join(source_path, i)
    sourcefile_modtimestamp = os.path.getmtime(sourcefile_path)
    sourcefile_modtime = datetime.utcfromtimestamp(sourcefile_modtimestamp)
    currenttime = datetime.now()
    sourcefile_modage = timedelta.total_seconds(currenttime - sourcefile_modtime)
    if sourcefile_modage >= 86400:
        shutil.move(source_path + '/' + i, destination_path)
        print(i + ' was sucessfully transferred.')
    else:
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        for i in source_files:
            shutil.move(source + '/' + i, destination)
            print(i + ' was sucessfully transferred.')




