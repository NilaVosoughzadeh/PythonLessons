list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 8, 9, 3]

for number1 in list1:
    for number2 in list2:
        if number1 == number2:
            print(f"{number1, number2} Are Intersection!")