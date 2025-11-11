#For loop
thislist = ["a" , "b" , 4 , True , "sdfkj"]
for x in thislist:
    print(x)

# Using Range
for i in range(len(thislist)):
    print(thislist[i])

#Using while loop
i=0
while i < len(thislist):
    print(thislist[i])
    i+=1

"""
a
b
4
True
sdfkj
"""