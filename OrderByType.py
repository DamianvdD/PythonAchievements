myList = ['Doei', True, 26, 3.9, 999, False, 2.3, 'Lets Go']

strings = []
integers = []
booleans = []
floats = []

for item in myList:
    if(type(item) == str):
        strings.append(item)
    elif(type(item) == int):
        integers.append(item)
    elif(type(item) == bool):
        booleans.append(item)
    else:
        floats.append(item)

print(myList)
print()
print(strings)
print(integers)
print(booleans)
print(floats)
