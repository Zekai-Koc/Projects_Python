# created on gitHub.

import os
clear = lambda: os.system('cls')
clear()

# print(chr(27)+'[2j')
# print('\033c')
# print('\x1bc')

# TASK
# Create a list consisting of Fibonacci numbers from 1 to 55. 
# The desired output is like :
# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



f = 1
s = 1

fibonacci = [f,s]

for i in range(2,10):

    f,s = s, f+s

    fibonacci.append(s)

print(fibonacci)




# x = int(input("Please enter the first number: "))
# y = int(input("Please enter the second number: "))

# z = int(input("Please enter the max. fibbonaci value: "))

# total_x_y = 0

# fibonacci = [x, y]

# while total_x_y < z:
#     total_x_y = x + y
#     fibonacci.append(total_x_y)
#     x = y
#     y = total_x_y

# fibonacci.pop()
# print(fibonacci)

# 1  1 
# 1 + 1 = 2

# x,        y,          total_x_y
# 1,        1,          2
#           x           y               total_x_y



