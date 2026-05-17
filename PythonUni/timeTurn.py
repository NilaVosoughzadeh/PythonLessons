number = int(input("Enter number: "))

hour = number // 3600
minute = (number % 3600) // 60
second = (number % 3600) % 60

print(f"{hour} : {minute} : {second}")