usersList = []

while True :
    userName = input("Name : ")
    if userName == "0":
        break
    userAge = input("Age : ")
    userCity = input("City : ")

    usersDictionary = {}
    usersDictionary["Name"] = userName
    usersDictionary["Age"] = userAge
    usersDictionary["City"] = userCity

    usersList.append(usersDictionary)
print("---------------------------------")

for user in usersList :
    for key in user:
        print(key, user[key])
print("---------------------------------")