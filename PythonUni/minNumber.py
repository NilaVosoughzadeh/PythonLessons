numberList = []
total = 0.0

numbers = int(input("How many numbers do you have? "))

print("\n")

for i in range(0, numbers):
    num = float(input("Enter number " + str(i+1) + " : "))
    numberList.append(num)
    total += num
print("User list is : ", numberList)

meanNumber = total / numbers
print("Mean = ", meanNumber)