number = 2005
print("Given number : ", number

while number > 0 :
    getLastDigit = number % 10
    number = number // 10
    print(getLastDigit, end=" ")