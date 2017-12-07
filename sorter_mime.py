#!/bin/python
import sys
import os
import shutil
import magic
import errno


def mv_stuff(inputlist):
    source = inputlist[0]
    ls_source = os.listdir(source)
    # list of all the only files in source directory ommiting subdirectories
    fileList = [f for f in ls_source if os.path.isfile(os.path.join(source, f))]

    maindict = {
        'VID': ['webm', 'mp4', 'avi', '3gp', 'mkv', 'srt', 'video'],
        'AUD': ['audio', 'mp3', 'ogg', 'wav', 'mpeg4'],
        'ASCII': ['txt', 'py', 'c', 'c++', 'cpp', 'java', 'asm', 'sh', 'js', 'text'],
        'DOCS': ['pdf', 'doc', 'docx', 'conf', 'pptx', 'epub'],
        'COMPRESS': ['zip', 'tar', 'tarxz', 'targz', 'gz', 'bz2', 'empty', 'rar', 'jar'],
        'IMAGES': ['image', 'png', 'jpg', 'jpeg', 'gif', 'img'],
        'PROGRAMS': ['application', 'run', 'rpm', 'bundle', 'exe', 'deb', 'bin', 'apk'], 'ISOs': ['iso', 'ova']
    }

    # create main folder
    newdict = source + inputlist[1]

    try:
        if os.path.exists(newdict):
            os.mkdir(newdict)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        # pass

    # create sub folders inside newly created main folder
    for key, value in maindict.iteritems():
        if not os.path.exists(os.path.join(newdict, key)):
            try:
                os.mkdir(os.path.join(newdict, key))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
                # pass
    # iterate through main dict check file extenstions and move files to respective directories
    for x, y in maindict.iteritems():
        for f in fileList:
            f = os.path.join(source, f)
            dest = os.path.join(newdict, x)

            if not os.path.exists(os.path.join(dest, f)):
                try:
                    if os.path.exists(f):
                        mime_get = magic.from_file(f, mime=True)
                        if any(element in mime_get for element in tuple(y)):
                            shutil.move(f, dest)

                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
                    # pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'please use it, like this # python {0} <sourcepath> <new folder name> '.format(__file__)
        sys.exit(0)
    mv_stuff(sys.argv[1:])
