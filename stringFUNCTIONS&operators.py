"""UPPER()"""
a = "zorro"
print(a.upper())
#>>>ZORRO



"""LOWER()"""
B = "SINAN"
print(B.lower())



"""The STRIP() method removes any whitespace from the beginning or the end:"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"



"""The REPLACE() method replaces a string with another string:"""
a = "Hello, World!"
print(a.replace("H", "J"))



"""Use the FORMAT() method to insert numbers into strings:"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#>>>My name is John, and I am  36
#EXAMPLE2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


"""ESCAPE CHARACTER
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:"""

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


""" *******ESCAPE CODES******* """
r""" \' Single Quote    e.g.; print("It\'s you!")
 \\ Backslash   e.g.; print("Backslash symbol is \\.")
 \n New Line    e.g.; print("New\nLine")
 \r Carriage Return e.g.; print("Ignored\rCounted")
 \t Tab e.g.; 
 \b Backspace   #This example erases one character (backspace):txt = "Hello \bWorld!" >>>HelloWorld



