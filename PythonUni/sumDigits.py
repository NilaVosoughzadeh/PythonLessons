def sumDigits(number):
    sumNumber = 0
    while number > 0:
        sumNumber += number % 10
        number // = 10
    return sumNumber

print(sumDigits(365))


print("اعداد 3 رقمی که مجموع ارقام آنها بر 3 بخش پذیر است : ")
for i in range(1, 1000):
    if sumDigits(i) % 3 == 0:
        print(i)