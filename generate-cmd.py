# -*- coding: utf-8 -*-
from os import walk
import os

path = os.getcwd() + '/'
properties = 'properties/'
sandboxes = []

def main():
    removeoldcmd()
    listsandbox()
    generate()

def removeoldcmd():
    for (dirpath, dirnames, filenames) in walk(path):
        for fn in filenames:
            if fn.endswith('.cmd'):
                os.remove(os.path.join(dirpath, fn))
        break

def listsandbox():
    global sandboxes
    for (dirpath, dirnames, filenames) in walk(path + properties):
        for fn in filenames:
            if fn.endswith('.properties'):
                sandboxes.append(fn[6:-11])
        break

def content(sandbox):
    result = """@echo off
set opt=
:looparg
if (%1) == () goto endloop
set arg=%1
if %arg:~0,2%==f- (
    set opt=%opt% -Dfile=%arg:~2%
) else if %arg:~0,2%==p- (
    set opt=%opt% -Dfolder=%arg:~2%
) else (
    set opt=%opt% %arg%
)
shift
goto looparg
:endloop
set opt=%opt:~1%
@echo on
"""
    result += 'ant -Dsandbox=' + sandbox + ' -propertyfile ./properties/build-' + sandbox + '.properties %opt%'
    return result

def generate():
    for sandbox in sandboxes:
        filepath = path + sandbox + '.cmd'
        with open(filepath, "w") as f:
            f.write(content(sandbox))
            f.close()

main()