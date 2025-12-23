# imports
import os
import glob

# variables
path1 = "C:/Windows/Temp/*"
path2 = "C:/Users/Martin/AppData/Local/Temp/*"

for file in glob.glob(path1):
    os.remove(file)