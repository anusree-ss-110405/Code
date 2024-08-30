# length of a number
# print(len(12345)) 
# TypeError: object of type 'int' has no len()

# Data Types
# String, Integer, Float, Boolean

# String = "Hello" [index or position]
# Start counting with 0
# Sub scripiting
print("Hello"[0])
print("Hello"[4])
# "123" is a string
# '+' concatenation
print("123"+"345")

# Integer - without any decimal places
print(123+345)
# Commas in numbers are replaced by underscores
print(123_455)

# Float - decimal number - as decimal point can float at any places
print(3.1234)

# boolean - True False

# num = len(input())
# print("Your name has "+num+" characters. ")
# TypeError: can only concatenate str (not "int") to str

# Type of data type
num = float(54)
print(type(num))

# Type conversion - Type casting
new_num = str(num)
print("Your num "+new_num)

print(70 + float("100.5")) # 170.5
print(str(70)+str(100))

# Operators
# Division always returns float

print(4 + 5)
print(8 - 9)
print(9 * 8)
print(9 / 3)
print(9 ** 8)

# PEMDAS
# ()
# **
# *
# /
# +
# -
print(3 + 3 - 3 * 3 / 3)

# BMI Calculation

height = input()
weight = input()
weighte = int(weight)
heighte = float(height)
bmi = weighte/heighte ** 2
print(int(bmi))

height = input()
weight = input()
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
# bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)

# 8/3 = 2.66666
# int(8/3) = 2
print(round(8/3)) # number next to it
print(round(8/3,2)) # round of two decimal places
print(8 // 3) # floor division chop of decimals
# // int / float
# += -= /= *=

# F string
agestr = input()
age = int(agestr)
total_weeks = 90*52;
remaining_age = 90 - age
remaining_weeks = remaining_age*52;
print(f"You have {remaining_weeks} weeks left.")

age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")