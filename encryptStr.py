text = input("Enter txt : ")

firstChar = text[0]
extraChar = text[1:-1]
endChar = text[-1]

encrypt = endChar + extraChar + firstChar

print(encrypt)