# if condition:
#     do this 
# else:
#     do this
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height > 120:
#     print("Eligible")
# else:
#     print("Not Eligible")
# if,else,colon :,indendation important
# > < >= <= == !=
# assignment && check equality


# NESTED IF CONDITION
# if condition:
#     if anothercondition:
#         do this
#     else:
#         do this
# else:
#     do this

# if / elif / else
#     if condition:
#         do A
#     elif conditon 2:
#         do C
#     else:
#         do B

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
if height > 120:
    age = int(input("Age ?"))
    if age < 12:
        print("Pay $5")
    elif age > 12 and age < 18:
        print("Pay $7")
    else:
        print("Pay $10")
else:
    print("Not Eligible")

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# Which year do you want to check?
year = int(input())
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# Instructions
# 💪 This is a difficult challenge! 💪
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.

# This is how you work out whether if a particular year is a leap year.

# on every year that is divisible by 4 with no remainder

# except every year that is evenly divisible by 100 with no remainder

# unless the year is also divisible by 400 with no remainder

# If english is not your first language or if the above logic is confusing, try using this flow chart .

# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)

# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)

# 2100 ÷ 100 = 21 (Not Leap)

# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, including spelling an punctuation.

# Example Input 1
# 2400
# Example Output 1
# Leap year
# Example Input 2
# 1989
# Example Output 2
# Not leap year
