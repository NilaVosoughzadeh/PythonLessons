L=[]
while 1:
    choose = input("choose: 1.add 2.remove \n")
    if choose == "1":
        name= input("name: ")
        L.append(name)
    elif choose == "2":
        name= input("name: ")
        L.remove(name)
    for i , name in enumerate(L,1):
        print(str(i)+ '.' ,name)