
# Dictionaries in python

# Create and print a dictionary:


thisdict = {
    "brand":"Suzuki",
    "model":"Swift",
    "Year":1999
}
print(thisdict)
print()

# Print the "brand" value of the dictionary:

print(thisdict["brand"])    # it will print the brand name
print()

# Duplicate values will overwrite existing values:

thisdict1 = {
    "brand":"Audi",
    "model":"A4",
    "year":1999,
    "year":2000
}
# year will be overwrite as 2000

print(thisdict1)
print()

# Print the number of items in the dictionary:

print("Length of thisdict1 is = ",len(thisdict1))
print()

# The values in dictionary items can be of any data type:

dict1 = {
    "Name":"Praveen",
    "Good_Boy":True,
    "year":2002,
    "colors": ["Black","white","blue"]
}

print(dict1)
print()

# From Python's perspective, dictionaries are defined as objects with the data type 'dict':

print("Type of data type dict1 is = ",type(dict1))
print()

# Access Dictionary Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

dict2 = {
    "Name":"Praveen Jha",
    "Sec":"B",
    "Department":"CSE",
    "year":"2nd"
}

# Get the value of the "Department" key:

x = dict2["Department"]
print(x)
print()

# There is also a method called get() that will give you the same result:

y = dict2.get("Department")
print(y)
print()

# The keys() method will return a list of all the keys in the dictionary.

x1 = dict2.keys()
print(x1)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:

my = {
    "name":"Praveen jha",
    "department":"CSE",
    "year":"2nd"
}
x2 = my.keys()
print("Before the change \n",x2)
print()
my["color"] ="Black","white","blue"
print("After the change \n",my)
print()

# The values() method will return a list of all the values in the dictionary.

y1 = my.values()
print(y1)
print()

# The items() method will return each item in a dictionary, as tuples in a list.

z = my.items()
print(z)
print()

# Check if "year" is present in the dictionary:

if "year" in my:
     print("yes, 'year' is one of the keys in the my dictonary")

# Change the "year" to 2018:

thisdict["Year"] = 2018
print(thisdict)
print()

# Update the "year" of the car by using the update() method:

thisdict.update({"year":2021})

print(thisdict)
print()

# Add Dictionary Items

thisdict["color"] = "red"
print(thisdict)
print()

# Add a color item to the dictionary by using the update() method:

thisdict.update({"color":"green"})
print(thisdict)
print()

# The pop() method removes the item with the specified key name:

thisdict.pop("model")       # this will remove the 'model'
print(thisdict)
print()

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.popitem()      # this will remove the last item from the dictonary
print(thisdict)
print()

# The del keyword removes the item with the specified key name:

del thisdict["year"]
print(thisdict)
print()

# The clear() method empties the dictionary:

print(thisdict1)
thisdict1.clear()   # it will clear the dictonaries
print(thisdict1)




