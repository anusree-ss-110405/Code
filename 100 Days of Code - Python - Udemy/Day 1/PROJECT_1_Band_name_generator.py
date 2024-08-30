print("Welcome to my band name generator!")
string1=input("What is the name of the city you grew up in? \n")
string2=input("What is your favorite pet name? \n")
print("Your band name could be " +string1 + " " + string2)

# Input Function and print() Issue:

# When you use input(), it already prints the prompt and waits for user input. You don't need print() around input().
# Assignment Issue:

# print() function returns None, so string1 and string2 are being assigned None.
# Concatenation Error:

# Even if print(input()) returned the input, you shouldn't use print() for assignment because it doesn't return the entered value directly.