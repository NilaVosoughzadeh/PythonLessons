length = "shahram"
print (len(length))
print (len("Hello World"))

#تغییر حالت رشته
print(length.upper())
print("nila".upper())
print("ARASH".lower())
name = "sArA"
newName = name.lower()
print(newName)

'''
country = input("Enter your country: ")
print(country.capitalize())
'''

text = "my name is nila"
print(text.title())

#شمارش رشته ها
str = "I love you honey"
print(str.count("o"))
word = "my name is nila, what is your name?"
print(word.count("name"))

#جابجایی
print(str.replace("honey","money"))

#indexing
language = "python"
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])

print(language[0:2])
print(language[2:])
print(language[::-1])

#برعکسش منفی است
print("nila"[-1])
print("nila"[-2])
print("nila"[-3])
print("nila"[-4])

print("nila ali zoha amirhossein".split())
print("mina-mona-minu".split("-"))

#Delete Space
print(" Hello ".strip())

#is alphabet
print("Hi84".isalpha())

#is number
print("84".isnumeric())

#check password
print("Nila84".isalnum())

print("Hi".startswith("h"))
print("Hi".endswith("i"))

#find index char
print("nila".find("a"))
print("Hello World".index(" "))
#find shows it and continue , index shows error
print("Hi".find("n"))
print("nilia".find("ilia"))

#slice
a = "amirhossein"
print(a[ : 4])
print(a[4 : 11])
#گام
print(a[ : 5 : 2])
print(a[-12 : ])

stringLooping = "Nila"
for word in stringLooping:
    print(word)