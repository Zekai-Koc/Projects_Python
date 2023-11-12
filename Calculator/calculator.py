op = int(input("""Enter an operation
        (1) for addition
        (2) for multiplication"""))

a = int(input("Enter the first value"))

b = int(input("Enter the second value"))

if (op == 1):
    print("a + b = ",a+b)
elif (op == 2):
    print("a*b = ", a*b)
else:
    print("Wrong option!")
