# firstRow1 = list(input("Enter1: "))
# firstRow2 = list(input("Enter2: "))
firstRow1 = input("Enter1: ").split()
firstRow2 = input("Enter2: ").split()

eye = 0
for i in range(len(firstRow1)):
    if firstRow1[i] == '1' and firstRow2[i] == '1':
        eye += 1
print(f"totalEye : {eye}")