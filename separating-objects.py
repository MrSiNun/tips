"""SEPERATING OBJECTS OF A LIST."""
############FOR
#define the variable
mynumber_list = ["A", "B", "C"]
for i in range(len(mynumber_list)):
    print(mynumber_list[i])

mystring_list = ['hello', 'you']
for obj in mystring_list:
    print(obj)

###############WHILE
"""by while loop"""
thislist = ["sinan", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i=i+1



#WITHOUT_COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for obj in fruits:
    if "a" in obj:
        newlist.append(obj)
print(newlist)

#WITH_COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if "a" in x]
print(newlist)


#############LIST COMPREHENTION
thislist = ["SEVIL", "SEVGI", "ABLALARIM"]
[print(x) for x in thislist]







