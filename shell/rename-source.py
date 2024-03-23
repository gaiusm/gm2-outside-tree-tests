#!/usr/bin/env python3

import glob, os
import codecs


def generateFileList ():
    filelist = []
    for extension in [".def", ".mod", ".DEF", ".MOD"]:
        filelist += glob.glob ("./**/*" + extension, recursive=True)
    return filelist


def tokenize (token):
    token = token.replace (';', '')
    token = token.replace ('[', '')
    if token.find ("(*") > 0:
        token = token[:token.find ("(*")]
    return token


def word (line, no):
    words = line.split ()
    count = 0
    for w in words:
        token = tokenize (w)
        if token != "":
            count += 1
            if count == no:
                return token
    return None


def getModuleName (filename):
    content = open (filename, 'rb').read ().decode ('ISO-8859-1')
    content = content.replace (chr (26), '')
    open (filename, 'w').write (content)
    lines = open (filename, 'r').readlines ()
    for line in lines:
        line = line.rstrip ()
        if word (line, 1) in ["DEFINITION", "IMPLEMENTATION"]:
            return word (line, 3)
        if word (line, 1) == "MODULE":
            return word (line, 2)
    return "none"


def makeNewFilename (filename, moduleName):
    parts = filename.split ('/')
    if len (parts) > 0:
        if len (parts[-1]) > len (".mod"):
            if parts[-1][-4:] in [".mod", ".MOD"]:
                return "/".join (parts[:-1] + [moduleName + ".mod"])
            if parts[-1][-4:] in [".def", ".DEF"]:
                return "/".join (parts[:-1] + [moduleName + ".def"])
    return moduleName


def renameModule (filename):
    moduleName = getModuleName (filename)
    newfilename = makeNewFilename (filename, moduleName)
    if filename != newfilename:
        os.system ("mv " + filename + " " + newfilename)
        print ("# mv " + filename + " " + newfilename)


def main ():
    for filename in generateFileList ():
        renameModule (filename)


main ()
