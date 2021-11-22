a = """" Hello There I'm Learning Python """
print(a)
a1  = ''''Hey How are you '''
print(a1)

# Strings are Array

x = "Praveen Kumar Jha"
print(x[2])         # it will print a

for x1 in "Praveen kumar jha":
    print(x1)

 # String Length

k = "Praveen kumar jha"
print(len(k))      #it will print length of c

txt = "The best things in life are free!"
print("free" in txt)        # it will print true if it will find "free" in txt otherwise it will print false

# checking by if statement

if "free" in txt:
    print("Yes , 'free' is present.")

# check if not

print("expression" not in txt)   # it will print true beacause expression is not present in txt.

# Checking by if condition
if "expression" not in txt:
    print("No , 'expression' is not present in txt")

# Slicing String

print(txt[2:5])        # it will print characters from 2 to position 5 not including 2 and 5

print(txt[:5])          # it will print from starting to position 4

print(txt[2:])          # get the characters from position 2 , and all the way to the end

print(txt[-5:-2])       # position of -5 = 'f' and position of -2 is 'e' so it will print the characters between 'f' to 'e'


# Modify String

print(x.upper())        # it will convert all characters of 'x' into uppercase

print(x.lower())        # it will convert all characters of 'x' into lowercase

x1 = "   Praveen kumar jha        "

# The strip() method removes any whitespace from the beginning or the end:

print("printing without removing white space \n ",x1)
print(x1.strip())        # it will print "Praveen kumar jha"

# Replace String

print(x.replace("P","T"))       # it will replace 'P' into 'T'

x2 = "Hello , Praveen !"
print(x2.split(","))        # it will split string into substring if it finds instances of the separator

# String Concatenation

a2 = "Hello"
b2 = "Praveen"
c2 = a2+b2
print(c2)       # it will print HelloPraveen

d2 = a2+" "+b2
print(d2)           # it will print Hello Praveen

# String Format

age = 20
# txt1 = "My name is Praveen , I am "+age     # we can't combine string and numbers like this
# print(txt1)

# Use format() method to insert numbers into String

txt1 = "My name is Praveen , and I am {}"
print(txt1.format(age))     # it will print 'My name is Praveen , and I am 20'.

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemo = 234
prince = 50.90
myOrder = "I want {} pieces of item {} for {} rupees."
print(myOrder.format(quantity,itemo,prince))

myOrder1 = "I want to pay {2} Rupees for {0} pieces of item {1}"
print(myOrder1.format(quantity,itemo,prince))

# To insert an character in a String use escape character'\'

txt2 = "We are so called \"programers\""
print(txt2)