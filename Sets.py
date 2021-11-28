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
print(thisset12);
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













