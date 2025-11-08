thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1]) # banana
print(thislist[-1]) # mango
print(thislist[2:5]) # 2(include) to 5(exclude) --> ['cherry', 'orange', 'kiwi']
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']  
print(thislist[-4:-1]) # -4(include) to -1(exclude) --> ['orange', 'kiwi', 'melon']

# Check if Item exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #Yes, 'apple' is in the fruits list
