>**sorter_man**
*Quick way to sort files in bulky directories*

Sort files based on extentions and MIME type as well.so if any file dont have extenstion still script gonna detect file type.

first it creates subfolder in current working directory and then sort files based of type and move them to subfolders in new directory.


There are two files

1.  sorter_mime.py - which sort files and move them.
2.  mover_undo.py - it can revert back moving operation(***warning***: it will move all the files from all subdirectories to parent directory)


**Prerequisites**
python 2.7/with few changes python3 as well


import shutil,sys,os,magic (required)

pip install shutil


pip install magic


**script in action**
[![sortman demo](https://img.youtube.com/vi/JneqRtPMsOc/0.jpg)](https://www.youtube.com/watch?v=JneqRtPMsOc)

