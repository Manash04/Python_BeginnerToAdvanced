#Append Items --> Used to append only at the end

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#Insert Items --> Used to insert the element at any specific index

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)    #['apple', 'banana', 'watermelon', 'cherry']

#Extend List -->  To append elements from another list to the current list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)    #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Anything can be added to list but list cant be added to anything.

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)   #['apple', 'banana', 'cherry', 'kiwi', 'orange']  

