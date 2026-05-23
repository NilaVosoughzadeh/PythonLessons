import random

randomNumbers = []

while len(randomNumbers) < 3:
    num = random.randint(100, 999):
    if num % 5 == 0:
        randomNumbers.append(num)
print(randomNumbers)