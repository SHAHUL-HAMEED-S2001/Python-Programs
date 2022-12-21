# Python Program to Find Sum of Digit of a Number using Recursion

class Program:
    def sumOfDigits(self,num):
        if (num<=0):
            return 0
        return (num%10) + sol.sumOfDigits(num//10)

val = int(input("Enter number to Find Sum of Digits of a Number: "))
sol = Program()

print("Sum of Digits of a",val,"is",sol.sumOfDigits(val))