import math
number = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "yes,given number ssis a perfect square")
else:
    print(number, "is not a perfect square")