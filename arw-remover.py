#!/bin/python

from tkinter import filedialog
import os

FILE_TYPE1 = ".jpg"
FILE_TYPE2 = ".arw"

def main():
    files_removed_count = 0
    
    removed_folder_name = "_removed/"

    directory = filedialog.askdirectory()
    print(directory)

    files_of_type1 = []
    files_of_type2 = []
    files_to_be_moved = []

    files = os.listdir(directory)
    for file in files:
        print(file)
        if FILE_TYPE1 in file:
            files_of_type1.append(file.replace(FILE_TYPE1, ""))
        elif FILE_TYPE2 in file:
            files_of_type2.append(file.replace(FILE_TYPE2, ""))

    for file in files_of_type2:
        if file in files_of_type1:
            continue
        else:
            old_path = os.path.join(directory, file + FILE_TYPE2)
            files_to_be_moved.append(old_path)

    # IF THERE ARE FILES TO BE MOVED
    if len(files_to_be_moved) > 0:
        
        # SEE IF NEED A NEW FOLDER NAME FOR THE FOLDER WITH REMOVED FILES
        removed_folder_path = os.path.join(directory, removed_folder_name)

        while os.path.isdir(removed_folder_path):
            removed_folder_name = "_" + removed_folder_name
            removed_folder_path = os.path.join(directory, removed_folder_name)

        # CREATE NEW FOLDER WITH THE NAME
        os.mkdir(removed_folder_path)

    print(files_to_be_moved)

    for file in files_to_be_moved:
        new_path = os.path.join(directory, removed_folder_name, os.path.basename(file))
        os.rename(file, new_path)
    
if __name__ == "__main__":
    main()
    
