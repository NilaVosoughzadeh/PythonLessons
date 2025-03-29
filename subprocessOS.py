import os
import subprocess

os.chdir("..")
dirs = subprocess.getoutput("dir").split()

print(dirs)

for i in dirs :
    if i == "<DIR>" :
        index = dirs.index(i)
        print(dirs[index+1])
        dirs.pop(index)