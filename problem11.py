# Write about data types and variables in python. explain the the data types with example.

# Variable :
# Variable are the form for a data which can be stored in a particular variable like a , b , c

# Variable example:- 

a = "Nischay"

# Data Types:- 
#  Data types means when we are entering a input. there are some conditions like we have to only enter the numbers then we use int-
# data types and for decimals we use float, for making a statement true or false we use bool data type. for complex numbers we use complex.
# and etc.

# Data types examples

# Int Data type:- 
# This data type is used to store numbers in it. Int means integer it can contain all non-decimal number.

x = int(input("Enter a number: "))

print(type(x))

# Output :- If I type 2. It prints 2. If i type 2.0 it shows a error. because it only allows the interger values.

# Str Data type:- 
# This data type is used to store a text in it. Str means string. 

# ex:- 

c = "I am Junior"
print(c)
print(type(c))

# Output:- I am printing c which print's I am Junior. because it is a str.

# float Data type:- 
# This data type is used to store numbers in it. float means decimal number it can contain all decimal numbers inclusing integers.

# Example
 
y = float(input("Enter a number: "))
print(y)

# output :- If I type 2. it prints 2.0. You can type any number in this as it allows everything.

# Bool Data type:
# This data type is used to tag a statement if it should work or no. 

# Ex:- 

Nischay = True
Shid = False

if Nischay:
    print("Yes")
else:
    print("No")

if Shid:
    print("Yes")
else:
    print("No")

# Here Nischay is tagged as true which will print the if. If Nischay was tagged false it would print the else value.


# Complex Data types:
# Complex data types are used for the mathematic equations like which contains variables in it.

# ex:- 

z = complex(input("Enter a value: "))
print(z)

# Output :- If I enter the 1 + 2i it takes the value it is assigned for it.




