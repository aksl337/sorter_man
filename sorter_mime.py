#!/bin/python
import sys
import os
import shutil
import magic
# import errno
# import re


def mv_stuff(inputlist):
    source = inputlist[0]

    # list of only files in source directory omitting subdirectories
    fileList = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

    # dictonary for folders as key and filetypes as values
    maindict = {
        'VID': ['webm', 'mp4', 'avi', '3gp', 'mkv', 'srt', 'video'],
        'AUD': ['audio', 'mp3', 'ogg', 'wav', 'mpeg4', 'mpeg'],
        'ASCII': ['txt', 'htm', 'py', 'c', 'c++', 'cpp', 'java', 'asm', 'sh', 'js', 'text', 'plain', 'shell'],
        'DOCS': ['pdf', 'doc', 'docx', 'conf', 'pptx', 'epub'],
        'COMPRESS': ['zip', 'tar', 'tarxz', 'targz', 'gz', 'bz2', 'empty', 'rar', 'jar'],
        'IMAGES': ['image', 'png', 'jpg', 'jpeg', 'gif', 'img'],
        'PROGRAMS': ['run', 'rpm', 'bundle', 'exe', 'deb', 'bin', 'apk'],
        'ISOs': ['iso', 'ova']
    }

    # create main folder
    newdirr = source + inputlist[1]
    os.chdir(source)
    if not os.path.exists(newdirr):
        os.mkdir(newdirr)

    # create sub folders inside newly created main folder
    for key, value in maindict.iteritems():
        if not os.path.exists(os.path.join(newdirr, key)):
            os.mkdir(os.path.join(newdirr, key))

    # iterate through main dict, check file extenstions and move files to respective directories
    for x, y in maindict.iteritems():
        dest = os.path.join(newdirr, x)
        fileList = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
        for f in fileList:
            in_files = os.path.join(source, f)
            mime_get = magic.from_file(in_files, mime=True)
            if os.path.exists(os.path.join(dest, f)):
                pass
            elif os.path.exists(in_files):
                if in_files.endswith(tuple(y)):
                    shutil.move(in_files, dest)
                elif any(element in mime_get.split("/")[1] for element in tuple(y)):
                    shutil.move(in_files, dest)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'please use it, like this # python {0} <sourcepath> <new folder name> '.format(__file__)
        sys.exit(0)
    mv_stuff(sys.argv[1:])
