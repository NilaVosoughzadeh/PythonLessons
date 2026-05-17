phoneNumber = input("Enter your phone number : ")

if phoneNumber.isnumeric():
    if len(phoneNumber) == 8:
        if phoneNumber.startswith("98" or "0"):
            print("Ok!")
        else:
            print("InCorrect")
    else:
        print("InValid")
else :
    print("Not Valid")