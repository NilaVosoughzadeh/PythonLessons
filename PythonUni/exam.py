#نیلا وثوق زاده - ملی مهارت قزوین - کارشناسی نرم افزار - آز زبان برنامه نویسی

#1
import random
number = random.randint(1, 5)
hads = 0
while hads != number:
    hads = int(input("hads bezan sisi : "))
print("Braaaaaaavo👍")


#2
beshmor = 0
print(f"Shomarande : {beshmor}")
yourName = ""
while yourName != "Nila":
    yourName = input("Plz Enter Ur Name : ")
    if yourName != "Nila":
        print("Answer is wrong!! think again dadash")
        beshmor += 1
        print(beshmor)
print("Ok Sisi <3")

#3
tupleName = ("Nila", "Mina", "Leila", "Nadia")
print(len(tupleName))
#3 b
while True:
    numberCast = input("Plz Enter Number : ")
    if numberCast.isnumeric():
        num = int(numberCast)
        print(int(num))
        print(type(num))
        break

#4
listAnimals = ["Dog", "Cat", "Monkey"]
listNumber = [2, 4, 6, 8, 10]
listAnimals.extend(listNumber)
print(listAnimals)