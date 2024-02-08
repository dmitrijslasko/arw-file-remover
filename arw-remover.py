#!/bin/python

from tkinter import filedialog
import os

FILE_TYPE_REFERENCE = ".jpg"  # file format to be used as a reference
FILE_TYPE_TO_BE_REMOVED = ".arw"  # file format to be removed

files_of_type1 = []
files_of_type2 = []
files_to_be_removed = []


def main():
    removed_folder_name = f"_removed-{FILE_TYPE_TO_BE_REMOVED}/"

    # LET THE USER TO PICK THE DIRECTORY WITH FILES
    directory = filedialog.askdirectory()

    files = os.listdir(directory)

    for file in files:
        if FILE_TYPE_REFERENCE in file:
            files_of_type1.append(file.replace(FILE_TYPE_REFERENCE, ""))
        elif FILE_TYPE_TO_BE_REMOVED in file:
            files_of_type2.append(file.replace(FILE_TYPE_TO_BE_REMOVED, ""))

    print(files_of_type1)
    print(files_of_type2)
    print(set(files_of_type1).difference(set(files_of_type2)))

    for file in files_of_type2:
        if file in files_of_type1:
            continue
        else:
            old_path = os.path.join(directory, file + FILE_TYPE_TO_BE_REMOVED)
            files_to_be_removed.append(old_path)

    # IF THERE ARE FILES TO BE MOVED
    if len(files_to_be_removed) > 0:

        # SEE IF NEED A NEW FOLDER NAME FOR THE FOLDER WITH REMOVED FILES
        removed_folder_path = os.path.join(directory, removed_folder_name)

        while os.path.isdir(removed_folder_path):
            removed_folder_name = "_" + removed_folder_name
            removed_folder_path = os.path.join(directory, removed_folder_name)

        # CREATE NEW FOLDER WITH THE NAME
        os.mkdir(removed_folder_path)

    print(files_to_be_removed)

    # MOVE THE FILES
    for file in files_to_be_removed:
        new_path = os.path.join(directory, removed_folder_name, os.path.basename(file))
        os.rename(file, new_path)


if __name__ == "__main__":
    main()
