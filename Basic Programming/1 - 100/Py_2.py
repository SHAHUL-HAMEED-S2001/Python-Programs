# Python Program to Check Whether a Given Number is Even or Odd using Recursion

class Program:
    def isEven(self, num):
        if (num < 2):
            return (num%2==0)
        return soln.isEven(num-2)

val = int(input("Enter a Number: "))
soln = Program()

if (soln.isEven(val)):
    print("Number is even!")
else:
    print("Number is odd!")