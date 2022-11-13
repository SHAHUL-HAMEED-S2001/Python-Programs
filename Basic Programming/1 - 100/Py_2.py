# Python Program to Check Whether a Given Number is Even or Odd using Recursion

class CheckEven:
    def __init__(self):
        pass

    def isEven(self, num):
        if (num < 2):
            return (num % 2 == 0)
        return (check.isEven(num - 2))

val = int(input("Enter a Number: "))

check = CheckEven()

if check.isEven(val):
    print("Number is even!")
else:
    print("Number is odd!")