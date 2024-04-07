
def factorial(number):
   if number == 0: return 1
   return number * factorial(number - 1)

print(factorial(5))


def factorial2(number):
   result = 1
   for i in range(1, number + 1):
      result *= i
   return result

print(factorial2(5))