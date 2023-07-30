myList = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "potato",
]
newList = []

for x in myList:
    if "a" in x:
        newList.append(x)

print(newList)

# Other method
fruits = ["apple", "banana", "cherry", "orange", "potato"]

newList = [x for x in fruits if "a" in x]
print(newList)
