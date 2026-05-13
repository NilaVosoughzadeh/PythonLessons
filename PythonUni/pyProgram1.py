#1
listNumber1 = [1, 2, 3, 4, 5, 6, 7]
listNumber2 = [10, 15, 20, 25, 30, 35, 40]

listMerge = []

for i, num in enumerate(listNumber1) :
    if num % 2 != 0:
        listMerge.append(num)

for i, num in enumerate(listNumber2) :
    if num % 2 == 0:
        listMerge.append(num)

print("New List : ", listMerge)