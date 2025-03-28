import os
import subprocess

result = subprocess.check_output('dir /S /B *.txt' , shell=True).decode(errors="replace").split()

print(result)

# Delete txt
for i in result :
    os.remove(i)