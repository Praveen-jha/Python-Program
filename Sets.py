# Sets in Python
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable* , and unindexed.

myset = {"Praveen", "banana", "cherry"}
print(myset)
print()

# Sets cannot have two items with the same value.

thisset = {"Praveen","banana","cherry","Praveen"}
print(thisset)
print()

# Get the number of items in a set:

print("length of the set is = ",len(thisset))

# Set items can be of any data type:

set1 = {"Praveen","banana","cherry"}
set2 = {1,2,3}
set3 = {True, False, True}

# A set can contain different data types:
set4 = {"Praveen",34,True,30,"male"}
print(set4)
print()

print(type(set4))       # it will print what type of set is

# Using the set() constructor to make a set:


thisset12 = set(("Praveen","Rajkumari","Mayank"))
print(thisset12)
print()


# Access Set Items
# You cannot access items in a set by referring to an index or a key.
# But you can through the set item using a for loop

for x in thisset12:
    print(x)
print()

# Check if "Praveen" is present in the set:
print("Praveen" in thisset12)

# To add one item to a set use the add() method.
thisset12.add("Perwez")     # 'Perwez' will be added in the list
print(thisset12)
print()

# Add elements from Set1 into Set2:

Set1 = {"Praveen","Perwez","Mayank","Rajkumari"}
Set2 = {"Pratik","Pawan","Sonu","Hasmatullah"}


Set1.update(Set2)       # items of Set2 will be added in Set1
print(Set1)
print()

# Add elements of a list to at set:

Myset = {"Praveen","Perwez","Rajkumai","Mayank"}
Mylist = ("Pratik","Pawan")
Myset.update(Mylist)    # it will add items of Mylist into Myset
print(Myset)

# Remove Set Items

# Remove "Pawan" by using the remove() method:
Myset.remove("Pawan")
print(Myset)
print()

# Remove "Pratik" by using the discard() method:

Myset.discard("Pratik")
print(Myset)
print()

# Remove the last item by using the pop() method:

print(thisset)
y = thisset.pop()       # it will remove 'Praveen' from the set
print(y)
print()
print(thisset)
print()

# The clear() method empties the set:

thisset.clear()     # to clear the set
print(thisset)
print()


# The del keyword will delete the set completely:
del thisset     # thisset will be deleted
#print(thisset)      # this will through an error

# Loop Sets
thisser = ("Praveen","Prakash","Sumit","Sahil")
for x in thisser:
    print(x)
print()


# Join Sets

# The union() method returns a new set with all items from both sets:

thisset2 = {"a","b","c"}
thisset3 = {1,2,3}
thisset4 = thisset2.union(thisset3)     # items of both set will be store in new set --thisset4
print(thisset4)
print()

# The update() method inserts the items in set3 into set4:
Set3 = {"a","b","c"}
Set4 = {1,2,3}
Set3.update(Set4)       # this will insert all the elements of Set4 in Set3
print(Set3)
print()


# Keep the items that exist in both set x, and set y:
set_x = {"apple","banana","cherry"}
set_y = {"google","banana","orange"}
set_x.intersection_update(set_y)  # it will print the item which is common in both set (set_x and set_y)
print(set_x)
print()

# Return a set that contains the items that exist in both set_x1, and set_y1:

set_x1 = {"apple","banana","cherry"}
set_y1 = {"google","banana","orange"}
setz = set_x1.intersection(set_y1)
print(setz)
print()


# Keep the items that are not present in both sets:

setx2 = {"apple","banana","orange","cherry"}
sety2 = {"google","microsoft","apple","cherry"}
setx2.symmetric_difference_update(sety2)
print(setx2)
print()


# Return a set that contains all items from both sets, except items that are present in both:

setx3 = {"Praveen","Mayank","Perwez","Pratik"}
sety3 = {"Pratik","Pawan","Hasmatullah"}
setz3 = setx3.symmetric_difference(sety3)
print(setz3)
print()


# Set Methods

# add()	   ------>    Adds an element to the set
# clear()	-------->    Removes all the elements from the set
# copy()	------->    Returns a copy of the set
# difference()	------>    Returns a set containing the difference between two or more sets
# difference_update()	------->    Removes the items in this set that are also included in another, specified set
# discard()	-------->    Remove the specified item
# intersection()	------------>   Returns a set, that is the intersection of two other sets
# intersection_update()	----------->    Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	----------->    Returns whether two sets have a intersection or not
# issubset()	----------->   Returns whether another set contains this set or not
# issuperset()	----------->    Returns whether this set contains another set or not
# pop()	    ------->   Removes an element from the set
# remove()      ----->	Removes the specified element
# symmetric_difference()	---------->     Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    ------>     inserts the symmetric differences from this set and another
# union()	    ------>     Return a set containing the union of sets
# update()	-------->       Update the set with the union of this set and others


