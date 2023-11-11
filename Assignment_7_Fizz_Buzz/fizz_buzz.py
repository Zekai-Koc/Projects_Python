# Created locally for committin to gitHub later...


# Task : Print the FizzBuzz numbers.

# FizzBuzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz",
# print the rest of the numbers unchanged.
# Output each value on a separate line.

import os
clear = lambda: os.system("clear")

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')

clear()


for i in range(1, 101):
    if (not (i % 3)) and (not (i % 5)):
        print(i, "FizzBuzz")
    elif (not (i % 3)):
        print(i, "Fizz")
    elif (not (i % 5)):
        print(i, "Buzz")
    else:
        print(i)
