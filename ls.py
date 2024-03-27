#APPEND()
"""Using the APPEND() method to append an item:"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



#INSERT(index_number, new_item)
"""To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:"""
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



#EXTEND()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



#REMOVE()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



###POP()
"""Remove the second item:"""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
"""Removes the last item when index is not defined"""
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



#DEL X[i]
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)




#WITHOUT_COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for obj in fruits:
    if "a" in obj:
        newlist.append(obj)
print(newlist)

#WITH_COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)