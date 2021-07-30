import os
import fnmatch
import difflib
import re
from idlecolors import *

import tkinter as tk
from tkinter import *
from tkinter import filedialog
import ctypes

# Function to choose folder and set rootFolderInitial and rootFolderDelta variables
def chooseFolder():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path

# Message box to notify user to select Initial Root Folder (rootFolderInitial)
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, "Please select the root folder of the initial files", "Choose Initial Folder", 0)

# Set rootFolderInitial to user's selected folder
rootFolderInitial = os.path.abspath(chooseFolder())

# Message box to notify user to select Delta Root Folder (rootFolderDelta)
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, "Please select the root folder of the delta files", "Choose Delta Folder", 0)

# Set rootFolderDelta to user's selected folder
rootFolderDelta = os.path.abspath(chooseFolder())

print('Compiling data, please wait...')

# Temp list to store all initial files; didn't want to do this but I was getting bugs when trying to dynamically add files to the InitialFilePaths list
TempInitialList = []

# Lists for the Intial and Delta file paths, these will be a 1-1 match when comparing files
InitialFilePaths = []
DeltaFilePaths = []

# Hostnames for all delta configs
DeltaNameList = []

# Add all delta files into the DeltaFilePaths list
for subdir, dirs, files in os.walk(rootFolderDelta):
    
    for file in files:
        DeltaFilePaths.append(os.path.join(subdir, file))
        
# For each file in the list, open the file, pull the 'hostname' string, remove 'hostname' (get the router/switch name by itself) strip all spaces/newlines and add the name to the DeltaNameList       
for fNames in DeltaFilePaths:
    
     with open(fNames, 'r') as dFileHostName:
            
            dFile_Name = dFileHostName.readlines()
            
            for i, line in enumerate(dFile_Name):
            
                if 'hostname' in line:
                    
                    DeltaNameList.append(dFile_Name[i].replace('hostname', '').strip())
 
# Add all initial files into a temp list.
for subdir, dirs, files in os.walk(rootFolderInitial):

    for file in files:
        TempInitialList.append(os.path.join(subdir, file))

# For each item in the DeltaNameList (router/switch names) open each file in the TempInitialList (Initial files). If the hostname of the file in TempInitalList matches with a name in DeltaNameList
# add the file from TempInitialList to the InitialFilePaths list. This isn't efficient but it works.
for items in DeltaNameList:
    
    for things in TempInitialList:
    
        with open(things, 'r') as IFileHostName:
        
            IFile_Name = IFileHostName.readlines()
            
            for i, line in enumerate(IFile_Name):
            
                if 'hostname' in line:
                
                    if IFile_Name[i].replace('hostname', '').strip() == items:
                        InitialFilePaths.append(things)

# There should now be a 1-1 config list match between InitialFilePaths and DeltaFilePaths, iterate through each and print the differences from
# InitialFilePaths to DeltaFilePaths, a (-) in green indicates something exclusive to Initial, a (+) indicates something exclusive to delta. A (-) immediately followed by (+) indicates
# a change in the string (partially similar).
i = 0

while i < len(InitialFilePaths):

    print(f"##########{InitialFilePaths[i]}##########")
    print(f"##########{DeltaFilePaths[i]}##########")
    print()
    

    with open(InitialFilePaths[i], 'r') as rFile1:
        f1_text = rFile1.readlines()

    with open(DeltaFilePaths[i], 'r') as rFile2:
        f2_text = rFile2.readlines()

    for line in difflib.unified_diff(f1_text, f2_text, fromfile=InitialFilePaths[i], tofile=DeltaFilePaths[i], lineterm = '\n', n = 5):
        if re.search("^[+]", line):
            printc(red(line))
        elif re.search("^-", line):
            printc(green(line))
        else:
             printc(black(line))
            
    i += 1
