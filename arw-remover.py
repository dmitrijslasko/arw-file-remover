#!/bin/python

from tkinter import filedialog
import os

FILE_TYPE1 = ".jpg"
FILE_TYPE2 = ".arw"

def main():
    removed_folder_name = "_removed/"
    directory = filedialog.askdirectory()
    print(directory)

    files_of_type1 = []
    files_of_type2 = []

    files = os.listdir(directory)
    for file in files:
        print(file)
        #print(type(file))
        if FILE_TYPE1 in file:
            files_of_type1.append(file.replace(FILE_TYPE1,""))
        if FILE_TYPE2 in file:
            files_of_type2.append(file.replace(FILE_TYPE2,""))

    removed_folder_path = os.path.join(directory, removed_folder_name)
    
    while os.path.isdir(removed_folder_path):
        removed_folder_name = "_" + removed_folder_name
        removed_folder_path = os.path.join(directory, removed_folder_name)
    
    os.mkdir(removed_folder_path)

    for file in files_of_type2:
        if file in files_of_type1:
            continue
        else:
            old_path = os.path.join(directory, file + FILE_TYPE2)
            new_path = os.path.join(directory, removed_folder_name, file + FILE_TYPE2)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    main()
    
