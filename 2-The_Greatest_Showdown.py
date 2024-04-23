# Task 1:

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
print("\nLargest number: " + str(max(num1, num2, num3)))

# Task 2:

print("Smallest number: " + str(min(num1, num2, num3)))

# Task 3:

if (num1 == num2 and num2 == num3):
    print("All numbers are the same")
elif (num1 == num2):
    print("There are 2 " + str(num1) + "'s equal to one another")
elif (num1 == num3):
    print("There are 2 " + str(num1) + "'s equal to one another")
elif (num2 == num3):
    print("There are 2 " + str(num2) + "'s equal to one another")