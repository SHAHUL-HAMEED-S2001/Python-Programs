# Python Program to Find Sum of Digits of a Number

class Program:
    def __init__(self):
        self.rem = 0
        self.add = 0

    def sumOfDigits(self,num):
        while(num>0):
            self.rem = num%10
            self.add = self.add + self.rem
            num //= 10    
        return self.add

val = int(input("Enter number to Find Sum of Digits of a Number: "))
sol = Program()

print("Sum of Digits of a",val,"is",sol.sumOfDigits(val))