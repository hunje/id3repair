#!/usr/bin/env pyathon2.7

import config
import sys
import os.path

def get_target_file(arg):
    if len(arg) <= 1:
        return None
    return os.path.abspath(arg[1])


def main():
    target = get_target_file(sys.argv)
    if target == None:
        print "Target file is not exist"
        exit(1)
    print "target file : %s" % target

if __name__ == '__main__':
    main()


