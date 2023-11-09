import os

clear= lambda:os.system('cls')

clear()



numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

most_frequent = [0, 0]

numbers.sort()

print(numbers)

# for i in range(0, len(numbers)):
#     temp_frequency = 0
#     for j in range(0, len(numbers)):  # change index to i instead of 0
    


#         if numbers[i] == numbers[j]:
#             temp_frequency += 1

#         if temp_frequency > most_frequent[1]:
#             most_frequent[0] = i
#             most_frequent[1] = temp_frequency
#         print(most_frequent)



    #     user_input = input("hit Enter")
    # print("xxxxxxxx")

        
# print("the most frequent number is {} and it was {} times repeated".format(most_frequent[0], most_frequent[1]))




# set_temporary = set(numbers)

# dictionary_frequency = dict()

# temp_most_frequent_number = [0, 0]

# for i in set_temporary:
#     temp_frequency = 0
#     for j in range(len(numbers)):
#         if i == numbers[j]:
#             temp_frequency += 1

#     dictionary_frequency["frequency of number " + str(i)] = temp_frequency
#     if temp_frequency > temp_most_frequent_number [1]:
#         temp_most_frequent_number[0] = i
#         temp_most_frequent_number[1] = temp_frequency
    
# print(temp_most_frequent_number)


# print("the most frequent number is {} and it was {} times repeated".format(temp_most_frequent_number[0], temp_most_frequent_number[1]))



# print(dictionary_frequency)
