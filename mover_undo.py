#!/bin/python
import os
import sys
import shutil


def mv_undo(inputList):
    dest = inputList[1]
    source = inputList[0]
    for root, directories, filenames in os.walk(source):
        for filename in filenames:
            filename = os.path.join(root, filename)
            shutil.move(filename, dest)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'python {0} <sourcepath(full absolute path)> <destpath (full absolute path)>'.format(__file__)
        sys.exit(0)
    mv_undo(sys.argv[1:])
