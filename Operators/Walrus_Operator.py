number = [1,2,3,4,5]
count = len(number)
if count >3:
    print(f"List has {count} elements")

#Output  --> List has 5 elements

#By using walrus operator := we can assign and use a value in the same expression

number1 = [1,2,3,4,5]
if(count := len(number1)) > 3:
    print(f"List has {count} elements")


"""List has 5 elements
List has 5 elements """