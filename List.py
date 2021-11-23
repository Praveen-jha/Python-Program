
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