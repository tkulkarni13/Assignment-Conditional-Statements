# Task 1:

year = int(input("Enter a year: "))
if (year % 400 == 0):
    print(True)
elif(year % 100 == 0):
    print(False)
elif (year % 4 == 0):
    print(True)
else:
    print(False)