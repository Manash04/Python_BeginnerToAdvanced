#and , or , not

x = ["apple" , "banana"]
y = ["apple" , "banana"]
z=x
print(x is y) #False
print(x is z) #True
print(x == y) #True

""" 
x and y both are different list even though they have same value stored
x --> points to List Object1 (Eg: memory location 0x001) 
y --> points to List Object2 (Eg: memory location 0x002) 

z=x (z just points to the same objects as x)
Both x and z refers to the same list in memory

is --> compares the memory location
== --> compares the value

"""