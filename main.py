#!/usr/bin/env pyathon2.7
# -*- coding: utf-8 -*-

import config
import sys
import os.path
import eyed3

def get_target_file(arg):
    if len(arg) <= 1:
        return None
    return os.path.abspath(arg[1])

def show_environment():
    print eyed3.LOCAL_ENCODING
    print eyed3.LOCAL_FS_ENCODING

def repair_id3_tag(file_name):
    audio_file = eyed3.load(file_name)

    artist = correct_broken_korean(audio_file.tag.artist)
    album = correct_broken_korean(audio_file.tag.album)
    album_artist = correct_broken_korean(audio_file.tag.album_artist)
    title = correct_broken_korean(audio_file.tag.title)
    print audio_file.tag.version
    print "Artist: %s" % artist
    print "Title: %s" % title
    print "Album: %s" % album
    audio_file.tag.artist = artist
    audio_file.tag.album = album
    audio_file.tag.title = title
    audio_file.tag.album_artist = album_artist
    audio_file.tag.update(encoding='utf-8')

def correct_broken_korean(word):
    try:
        converted = word.encode('latin-1').decode('euc-kr')
    except:
        # It should be correct korean. 
        converted = word

    if word != converted:
        print "Detected broken Korean"

    return converted


def main():
    show_environment()
    target = get_target_file(sys.argv)
    if target == None:
        print "Target file is not exist"
        exit(1)
    print "target file : %s" % target

    repair_id3_tag(target)

if __name__ == '__main__':
    main()


