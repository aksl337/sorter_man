#!/bin/python
import os
import sys
import shutil


def mv_undo(inputList):
    for root, directories, filenames in os.walk(inputList[0]):
        for filename in filenames:
            filename = os.path.join(root, filename)
            shutil.move(filename, inputList[0])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'python {0} <sourcepath(full absolute path)>'.format(__file__)
        sys.exit(0)
    mv_undo(sys.argv[1:])
