import os
clear = lambda: os.system("clear")

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')

clear()



# Task : Print the prime numbers which are between 1 to entered limit number (n).

# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


user_input = int(input("Enter an upper limit: "))
list_prime_numbers = list()
total_iteration_number = 0          # (optional) for checking the code optimization

for outher_loop in range(2, user_input):
    is_prime = False
    total_iteration_number += 1
    for inner_loop in range(2, outher_loop):
        total_iteration_number += 1
        if not (outher_loop % inner_loop):
            is_prime = True
            break
    if not is_prime: 
        list_prime_numbers.append(outher_loop) 

print(list_prime_numbers)
print("total iteration number: ", total_iteration_number)


# (almost) same code with less iteration
user_input = int(input("Enter an upper limit: "))
list_prime_numbers = list()
total_iteration_number = 0          # (optional) for checking the code optimization

for outher_loop in range(2, user_input):
    is_prime = False
    total_iteration_number += 1
    max_range_for_inner_loop = (outher_loop // 2) + 1       # decreasing the iterations
    for inner_loop in range(2, max_range_for_inner_loop):
        total_iteration_number += 1
        if not (outher_loop % inner_loop):
            is_prime = True
            break
    if not is_prime: 
        list_prime_numbers.append(outher_loop) 

print(list_prime_numbers)
print("total iteration number: ", total_iteration_number)
