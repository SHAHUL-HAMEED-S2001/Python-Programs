# Python Program to Reverse a Number

class Reverse:
    def __init__(self):
        self.rem = 0
        self.add = 0

    def printReverse(self,num):
        print("Reversed Number of",num,"is ",end="")
        while(num>0):
            self.rem = num%10
            print(self.rem,end="")
            num //= 10

val = int(input("Enter a number to reverse: "))
sol = Reverse()
sol.printReverse(val)