#The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  #['apple', 'cherry']

#If there are more than one occurrence then remove 1st banana.
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)   #['apple', 'cherry', 'banana', 'kiwi']

#The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  #['apple', 'cherry']

#If Index not specified then it removes from the last.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']  

#The del() keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)   #['banana', 'cherry']

#del() keyword can also delete the list completely 
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #This will return name error bcoz it deleted the list completely

#The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]


