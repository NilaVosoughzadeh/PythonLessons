listNumber1 = [1, 2, 3, 4, 5, 6, 7]
listNumber2 = [10, 15, 20, 25, 30, 35, 10]

def checkList1(listNumber1):
    if listNumber1[0] == listNumber1[-1]:
        print(f"first num is : {listNumber1[0]} and last num is : {listNumber1[-1]} -- So it's")
        return True
    else :
        print(f"first num is : {listNumber1[0]} and last num is : {listNumber1[-1]} -- So it's")
        return False

def checkList2(listNumber2):
    if listNumber2[0] == listNumber2[-1]:
        print(f"first num is : {listNumber2[0]} and last num is : {listNumber2[-1]} -- So it's")
        return True
    else :
        print(f"first num is : {listNumber2[0]} and last num is : {listNumber2[-1]} -- So it's")
        return False

print(checkList1(listNumber1))
print(checkList2(listNumber2))