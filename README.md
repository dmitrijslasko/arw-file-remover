# ARW FILE REMOVER
Python script initially written for sorting photoshoot files for Sony cameras.
<br>

This Python script removes ARW files that don't have a corresponding JPG file with same name inside the same folder.\
(After you have selected the files you want to keep)

For example, if you have file1.jpg and file1.arw and file2.arw in a folder, the script will remove the file2.arw file but keep the file1.arw file.

**It will create a folder named "_removed" and move all the files there.**\
**If a folder named "_removed" already exists and is not empty, it will create folder named "__removed"..**

**After all obsolete files are sorted & moved to the new folder, you can safely remove the files yourself.**\
**This is to ensure you are the one to blame if you delete something you need. ;).**

It can be also used for removing other types of files (you will have to change the file extension inside the code).
