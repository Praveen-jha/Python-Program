
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

myTuple = ("Praveen","Tania","Mayank","Rajkumari")
print(myTuple)
print()

# Tuples allow duplicate values:

myTuple1 = ("Praveen","Tania","Mayank","Rajkumari","Praveen")
print(myTuple1)
print()

# Print the number of items in the tuple:

print("length of myTuple1 is = ",len(myTuple1))
print()

# we can make a tupple with one item but we have to give comma for it
thisTupple = ("Praveen",)       # this is tuppple
print(type(thisTupple))
print()

 # not a tupple

thisTupple1 = ("Praveen")       # thsi is String not a tupple
print(type(thisTupple1))
print()

# Tuple items can be of any data type:

tuple1 = ("Praveen","Tania","Mayank","Rajkumari")
tuple2 = (1,2,3,4)
tuple3 = (True,False,False)
print(tuple1)
print(tuple2)
print(tuple3)
print()

# A tuple can contain different data types:

tuple4 = ("Praveen","Tania",34,56,True,True,40,"male","female")
print(tuple4)
print()

# Using the tuple() method to make a tuple:

thisTupple2 = tuple(("Praveen","Tania","Mayank","Rajkuamri"))
print(thisTupple2)
print(type(thisTupple2))
print()

# Print the second item in the tuple:
print("Second item in thistupple2 is = ",thisTupple2[1])
print()

# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

print(thisTupple2[-1])
print(thisTupple2[-2])
print()

thistuple = ("Praveen","Tanai","Mayank","Rajkumari","Perwez","TanuPriya","Pawan")
print(thistuple[2:5])
print()
# This will Print items from the beginning to index 3 , but NOT included, "Perwez":
print(thistuple[:4])
print()

# Print all the elements from index 2 'Mayank' to the end
print(thistuple[2:])
print()

# print all the element from index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1])
print()

# To determine if a specified item is present in a tuple use the 'in' keyword:
if "Praveen" in thistuple:
    print("Yes, 'Praveen' is in the thisTuple")
print()

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Convert the tuple into a list to be able to change it:

x = list(thistuple)     # change thistuple into list
x[5] = "Praveen"        # changing the value of index 5
thistuple = tuple(x)    # changing thistuple into tuple again
print(thistuple)        # print thistuple
print()

# since tuple are immutable , if you want to add items in tuples first change it into list and then add items in it and again change it again to tuple

y = list(thistuple)
y.append("Pratk")
thistuple = tuple(y)
print(thistuple)

# Here if we want to add items in tuple we have to change the tuple into list , But we can add to tuples
# make a tuple and again make another tuple to add items in first tuple

firstTuple = ("Praveen","Tania","Mayank","Rajkumari","Hasmatullah","Sonu")
print("print first tuple before adding\n",firstTuple)
print()
secondTuple = ("Perwez","Pawan","Pratik")
firstTuple += secondTuple   # adding two tuples
print("printing tuple after adding \n",firstTuple)
print()

# As we can't add item in tuple , we also can't remove items from tuples
# for remove items from tuples first convert it into list then remove

thistuple1 = ("Praveen","Mayank","Perwez","Pawan","Hasmatullah","Sonu","Pratik")
z = list(thistuple1)
print("Print tuple before remove items\n",thistuple1)
print()
z.remove("Sonu")
thistuple1 = tuple(z)
print("Printing items after remove 'Sonu' from the tuple\n",thistuple1)
print()

# You can delete the tuple completely
Tuple = ("Hasmatullah","Sonu","Pawan")
print(Tuple)
# deleting the Tuple
del Tuple
# print(Tuple)    # this will show an error

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple","banana","cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Unpacking a tuple:
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

# Assign the rest of the values as a list called "red":
fruits1 = ("apple","banana","cherry","strawberry","raspberry")
(green1, yellow1, *red1) = fruits
print(green1)
print(yellow1)
print(red1)
print()

# Add a list of values the "yellow" variable:

(green2, *yellow2, red2) = fruits1
print(green2)
print(yellow2)
print(red2)
print()

# Loops in Tuples

# Iterate through the items and print the values:

fruits2 = ("apple","banana","cherry")
for x in fruits2:
    print(x)
print()


# Loop Through the Index Numbers
for i in range(len(fruits2)):
    print(i," = ",fruits2[i])
print()

# Using a While Loop
i = 0
while i < len(fruits2):
    print(i," = ",fruits2[i])
    i = i+1
print()

# To join two or more tuples you can use the + operator:

tple1 = ("a","b","c")
tple2 = (1,2,3)
tple3 = tple1+tple2
print(tple3)
print()

# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
tple4 = ("apple","banana","cherry")
mytple = tple4*2
print(mytple)
print()

# Python has two built-in methods that you can use on tuples.

# count()	  ------>   Returns the number of times a specified value occurs in a tuple
# index()	    ------->    Searches the tuple for a specified value and returns the position of where it was found







