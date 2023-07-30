# Loop through the list
thisList = ["appla", "banana", "cherry"]
for x in thisList:
    print(x)

# Loop through the next number
myList = [
    "potato",
    "mango",
    "cocoyam",
]
for i in range(len(myList)):
    print(myList[i])

# Using while loop
myList = ["apple", "banana", "cherry", "mango", "potatos"]

i = 0
while i < len(myList):
    print(myList[i])
    i = i + 1

# Looping using list comprehension
myList = ["apple", "banana", "cherry", "mango"]
[print(x) for x in myList]
