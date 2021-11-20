x = 1         #int
y = 2.8       #float
z = 1j        #complex

# To verify the type of any object in python , use the type() function
print("Type of ",x," is = ",type(x))
print("Type of ",y," is = ",type(y))
print("Type of ",z," is = ",type(z))
print()

# Integer is a whole number ,positive or negative , without decimal , of unlimited length

a = 1
b = 2345678987654
c = -23456
print("The Type of",a," is = ",type(a))
print("The Type of ",b," is = ",type(b))
print("The Type of ",c," is = ",type(c))
print()

# Float is a number ,positive or negative , containing one or more decimals
d = 1.11
e = 1.0
f = -45.565

print("The Type of",d," is = ",type(d))
print("The Type of",e," is = ",type(e))
print("The Type of",f," is = ",type(f))
print()

# Float can also be scientific numbers with an "e" to indicate the power of 10.
g = 35e3
h = 123E5
i = -98.76e345
print("The Type of ",g," is = ",type(g))
print("The Type of ",h," is = ",type(h))
print("The Type of ",i," is = ",type(i))
print()

# Complex numbers are written with a "j" as the imaginary part:
k = 4+9j
l = 5j
m = -5j

print("The Type of ",k," is = ",type(k))
print("The Type of ",l," is = ",type(l))
print("The Type of ",m," is = ",type(m))
print()

# Type Conversion

x1 = 1        # int
y1 = 2.567    # float
z1 = 23j       # complex

# convert from int to float

a1 = float(x1)

# convert from float to int

b1 = int(y1)

# convert from int to complex

c1 = complex(x1)

print(x1," converted to float --->",a1)
print(y1," converted to int ---->",b1)
print(z1," converted to complex --->",c1)
print()

print("The Type of ",a1," is = ",type(a1))
print("The Type of ",b1," is = ",type(b1))
print("The Type of ",c1," is = ",type(c1))
print()

# Printing Random Number

import random
print("Random Number Between 1 to 10 is = ",random.randrange(1, 10))

