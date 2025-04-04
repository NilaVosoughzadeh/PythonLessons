import os
from colorama import Fore

#CWD : Current Working Directory
cwd = os.getcwd()
print(Fore.YELLOW + cwd + Fore.RESET)

#Change Directory
# os.chdir("..")
# cwd = os.getcwd()
# print(Fore.RED + cwd + Fore.RESET)

# Create Folder
# path = os.path.join(cwd , "PythonFolder")
# os.mkdir(path)

#Remove Folder
# os.chdir("..")
# cwd = os.getcwd()
# path = os.path.join(cwd,"Python")
# os.rmdir(path)

#Remove File
# cwd = os.getcwd()
# path = os.path.join(cwd , "Hello text")
# os.remove(path)