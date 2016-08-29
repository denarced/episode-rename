#!/usr/bin/env python3

import os
import sys


def epNums(name, season):
    counter = 1
    while True:
        yield '%s-%s%02d' % (name, season, counter)
        counter += 1


def rename(name, season, files):
    for filename, epname in zip(files, epNums(name, season)):
        pieces = filename.split('.')
        ext = pieces[len(pieces) - 1]
        origDir = os.path.dirname(filename)
        print(filename, os.path.join(origDir, epname + '.' + ext))


def printHelp(appName):
    print('Usage: {} {{name}} {{season}} {{file}} [{{file}}...]'.format(
        appName))
    print('Example: {} firefly 1 1.mkv 2.mkv 3.mkv'.format(appName))

if __name__ == '__main__':
    # at least three params
    if len(sys.argv) < 4:
        print('not enough parameters')
        printHelp(sys.argv[0])
        sys.exit(2)
    name = sys.argv[1].strip()
    seasonStr = sys.argv[2].strip()
    files = sys.argv[3:]

    if len(name) == 0:
        print('name cannot be empty')
        sys.exit(3)

    try:
        season = int(seasonStr)
        assert season > 0
    except:
        print('season must be a positive number')
        sys.exit(4)

    for each in files:
        if not os.path.exists(each):
            print('file does not exist:', each)
            sys.exit(5)

    rename(name, season, files)
