# To print Hello World 3 times

print("Hello World!")
print("Hello World!")
print("Hello World!")

# What if to print 100 times

print("Hello World!\nHello World!\nHello World!")
print("A 'Single Quote' printed inside double quote")
print('A "Double quote" printed inside single quote')
print("Alternatively you can just \"escape \" the quote")

# Concatenation

print("Hello"+"Anu")
print("Hello "+"Anu")
print("Hello"+" Anu")
print("Hello"+" "+"Anu")

# Indendation is important

# Input function prompt for user

input("What's y'r name? ")
print("Hello "+input("What's y'r name? "))

# Hashtag or pound sign

print(input())
print(input())
print(input())

#length
print(len("Anusree"))

numlength=len(input())
print(numlength)

#variable

name=input("What's y'r name? ")
length=len(name)
print(length)

name = "Anusree"
print(name)
name = "Hemasree"
print(name)

# It prints Hemasree

# SWAPPING TWO VARIABLES
a = input()
b = input()
a,b=b,a
print("a: " + a)
print("b: " + b)

# There are two variables, a and b
a = input()
b = input()
# Create a third variable to help switch the values
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

# Explanation
# This technique utilizes Python's tuple packing and unpacking feature. Here's how it works:
# 1. Tuple Packing:
# The right-hand side of the expression b, a creates a tuple containing the values of b and a.
# 2. Tuple Unpacking:
# The left-hand side a, b unpacks the values from the tuple and assigns them to the variables a and b respectively.
# This effectively swaps the values of a and b without needing a temporary variable.