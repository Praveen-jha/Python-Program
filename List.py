
myList = ["Praveen","pawan","mayank"]
print(myList)
print("length of List is = ",len(myList))      # length of myList

list1 = ["Praveen","Pawan","perwez","mayank","Rajkumari"]
list2 = [1,2,3,4,5,6]
list3 = [True,False,False]

# List with Strings , Integers and Boolean values

list4 = ["Praveen",34,True,"Male"]
print(list4)

print(type(myList))     # it will print type of myList

thisList = list(("Tania","Praveen","Pratik","Pawan","Bablu","Mayank","Sonu","Hasmatullah"))       # we can create a new list by using list()
print(thisList)

print(thisList[1])          # it will print 'pawan' which is on index 1
print(thisList[-1])         # it will start from last

thisList1 = ["Praveen","Pawan","Perwez","Pratik","Hasmatullah","Mayank","Sonu"]

# Printing list using range
# We can print the items of list in a range


print(thisList1[2:5])       # it will print from index 2 to 4
print(thisList1[:4])        # it will print from starting to index 3
print(thisList1[2:])        # it will print index 2 to end
print(thisList1[-4:-1])     # it will print from -4 to -1 {not including -1(Sonu)}


# Check if item is available in list


if "Praveen" in thisList1:
    print("Yes , 'Praveen' is in the list")

# Change the item Value

print("Printing list before Replace\n",thisList)

thisList[2] = "Perwez"      # it will replace 'Pawan' to 'Perwez'

print("Printing list after Replace\n",thisList)

# Changing the value of list in a range

print("Printing list before replace\n",thisList)

thisList[2:5] = ["Rajiv","Raushan","Rajkumari"]     # it will replace from 2 to 4

print("Printing list after replace\n",thisList)

thisList [2:5] = ["Praveen"]        # it will replace 3 items into one item  , it will replace Rajiv , Raushan , Rajkumari into single item Praveen
print(thisList)

# Insert an Item at the specified index

thisList.insert(6,"Rajkumari")      # it will add Rajkumari at the end beacause there were no index 6 so it add an index 6
print(thisList)

thisList.insert(2,"Rajiv")          # it will raplace index 2 into Rajiv
print(thisList)

# To append elements from another list to the current list

thisList2 = ["Tania","Praveen","Mayank","Rajkumari","Pawan"]
thisList3 = ["Hasmatullah","Perwez","Pratik"]

thisList2.extend(thisList3)         # it will add 'thisList2' and 'thisList3'
print(thisList2)

# The extend() method does not have to append lists,you can add any iterable object (tuples , sets , dictionaries etc)

thisTupple = ("Perwez","Pratk")
thisList2.extend(thisTupple)        # it will add thisList2 and thisTupple
print(thisList2)

# The remove() method removes the specified item

thisList2.remove("Pawan")       # it will remove the 'Pawan' from the list
print(thisList2)

# The pop() method removes the specified index

thisList3.pop(1)        # it will remove 'Perwez' from the list
print(thisList3)

# Remove the last item

thislist = ["Praveen","Tania","Mayank","Rajkumari","Pawan"]
thislist.pop()      # it will remove the 'Pawan' from the list
print(thislist)

thislist.insert(4,"Pawan")      #'Pawan' will be added in the list at 4th index
print(thislist)
# The del keyword also removes the specified index

del thislist[4]     # 'Pawan' will be deleted from the list
print(thislist)

# Clear the list item , The list still remains ,but it has no content

thislist.clear()         # it will clear all items from the list
print(thislist)
print()

# Loop Through a List

thislist = ["Praveen","Tania","Mayank","Rajkumari","Pawan"]

for x in thislist:
    print(x)
print()

# Print all items by referring to their index number
for i in range(len(thislist)):
    print(thislist[i])
print()

# Print all items, using a while loop to go through all the index numbers
i=0;
while i< len(thislist):
    print(thislist[i])
    i+=1
print()
# A short hand for loop that will print all items in a list:

[print(x) for x in thislist]

# we can short a list into a new list , containing only the fruits with the letter "a" in the name

fruits = ["apple","banana","mango","kiwi","cherry"]     # make a list
fruits.append("litchi")         # add an item in a list
print(fruits)           # printing the list

# first create a new empty list
newList = []

for x in fruits:
     if "a" in x:
         newList.append(x)
print(newList)      # it will not print 'litchi' beacause there is no "a" in litchi
print()

# shortest code for this
# Syntax
# newlist = [expression for item in iterable if condition == True]

newlist1 = [x for x in fruits if "a" in x]
print(newlist1)
print()

# With no if statement then it will print all the items in the list

newlist2 = [x for x in fruits]
print(newlist2)
print()

# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:

newlist3 = [x for x in range(10)]
print(newlist3)     # it will print  0 to 9
print()

# Printing same with condition

newlist4 = [x for x in range(10) if x < 5 ]
print(newlist4)         # it will print 0 to 4
print()

# Set the values in the new list to upper case:

newlist5 = [x.upper() for x in fruits]  # it will store all items of fruits in newlist5 and convert all items in uppercase
print(newlist5)
print()

# Set all values in the new list to 'Praveen':
newlist6 = ['Praveen' for x in fruits]
print(newlist6)
print()

# Return "orange" instead of "banana":
newlist7 = [x if x != "banana" else "orange" for x in fruits]       # it will return 'orange' insted of 'banana'
print(newlist7)

# Sort List Alphanumerically
# Sort the list alphabetically:

fruits1 = ["orange","mango","kiwi","pineapple","banana"]
fruits1.sort()
print(fruits1)
print()

# Sort the list numerically:

numberList = [100,40,20,70,3,50,6]
numberList.sort()
print(numberList)
print()

# Sort the list descending:

fruits1.sort(reverse=True)
print(fruits1)

# Sort the list descending:

numberList.sort(reverse=True)
print(numberList)
print()

# Customize Sort Function
# The function will return a number that will be used to sort the list (the lowest number first):

def myfunction(n):
    return abs(n-50)
numberList1 = [100,30,5,60,3]
numberList1.sort(key=myfunction)
print(numberList1)
print()

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

fruits2 = ["banana","Orange","Kiwi","cherry"]
fruits2.sort()
print(fruits2)
print()

# The reverse() method reverses the current sorting order of the elements.

fruits2.reverse()
print(fruits2)
print()

 # Copy Lists

fruits3 = fruits2.copy()       # it will copy all items of fruits2 in fruits3 list
print(fruits3)
print()

# Make a copy of a list with the list() method:

fruits4 = list(fruits3)
print(fruits4)
print()

# Join Two Lists

joinList = ["a","b","c"]
joinList1 = [1,2,3]
joinList2 = joinList+joinList1
print(joinList2)
print()

# Append joinList1 into joinJist1:

for x in joinList1:
    joinList.append(x)
print(joinList)
print()

# Use the extend() method to add joinList1 at the end of joinList:

joinList.extend(joinList1)
print(joinList)
print()

# Python has a set of built-in methods that you can use on lists.

# append()   ----->	Adds an element at the end of the list
# clear()	----->  Removes all the elements from the list
# copy()	---->  Returns a copy of the list
# count()	---->  Returns the number of elements with the specified value
# extend()	---->   Add the elements of a list (or any iterable), to the end of the current list
# index()	------>  Returns the index of the first element with the specified value
# insert()	---->  Adds an element at the specified position
# pop()	-----> Removes the element at the specified position
# remove()	-----> Removes the item with the specified value
# reverse()	------> Reverses the order of the list
# sort()	----->  Sorts the list









