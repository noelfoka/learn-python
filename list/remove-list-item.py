# List items
myList = ["apple", "banana", "orang", "cherry"]

# Remove "banana"
myList.remove("banana")
print(myList)

# Remove the second item
myList.pop(1)
print(myList)

# Remove the last item
myList.pop()
print(myList)

# Remove the first item
thisList = [
    "apple",
    "orange",
    "cherry",
]
del thisList[0]
print(thisList)

# Delete the entire list
list = ["apple", "banana", "orange", "cherry"]
del list
print(list)
