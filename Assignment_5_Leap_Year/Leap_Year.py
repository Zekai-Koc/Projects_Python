# Clarusway Python Course: Assignment 5 on Collections.

# Task: Find out if a given year is a "leap" year or not with Python. (without using if-else blocks ore loops) (don't use if-else or any loop)

# In the Gregorian calendar, three criteria must be taken into account to identify leap years:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year; unless...
# The year is also evenly divisible by 400. Then it is a leap year.
# According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
# Write a Python program that prints True if the given year by the user is a leap year, prints False otherwise.
# Note that; this question is famous on the web, so that do it yourself to get more benefits from it.

# Created by Python 3.8.2 
# Libraries: no library imported.




# METHOD-1: Shortest solution (wihtout any if-else block or loop)

check_year = int(input("Please input a year for checking if it is leap or not: "))

print((check_year % 4 == 0) and (not (check_year % 100 == 0) or  (check_year % 400 == 0)))



# METHOD-2: More systematic approach

check_year = int(input("Please input a year for checking if it is leap or not: "))

dividable_4 = (check_year % 4 == 0)
dividable_100 = (check_year % 100 == 0)
dividable_400 = (check_year % 400 == 0)

leap_year = dividable_4 and (not dividable_100) or dividable_400

print(leap_year)


# MEHTOD-3 with if-else blocks

check_year = int(input("Please input a year for checking if it is leap or not: "))

dividable_4 = (check_year % 4 == 0)
dividable_100 = (check_year % 100 == 0)
dividable_400 = (check_year % 400 == 0)

if dividable_4:
    if (dividable_100):
        if (dividable_400):
            leap_year = True
        else:
            leap_year = False
    else:
            leap_year = True
else:
    leap_year = False

print(leap_year)
