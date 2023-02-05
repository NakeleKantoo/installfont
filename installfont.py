#!/usr/bin/python
import sys
import os
args = sys.argv
localflag=False
if args[1]=="":
    print("No font selected!")
    exit()
if args[1]=="-l":
    localflag=True
local=""
arg=""
if localflag:
    local="~/.local/share/fonts/"
    arg=args[2]
else:
    local="/usr/local/share/fonts/"
    arg=args[1]
os.system("mv "+arg+" "+local)
print("Font "+arg+" installed!")