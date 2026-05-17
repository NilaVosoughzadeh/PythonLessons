names = ["Nila", "Arash", "Vania"]

scores = [10, 20, 7]

for i, x in enumerate (names):
    print(x, "*" * scores[i])

for i, name in enumerate (names):
    print(f'name index {i} : {name} ')

colorList = ["Red", "Blue", "White"]
numList = list(enumerate(colorList))
print(numList)