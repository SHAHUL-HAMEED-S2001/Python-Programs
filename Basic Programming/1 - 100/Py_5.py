# Python Program to Reverse a Number

class Reverse:
    def __init__(self):
        self.rem = 0
        self.add = 0

    def printReverse(self,num):
        print("Reversed Number of",num,"is ",end="")
        """
        The end parameter in the print function is used to add any string. 
        At the end of the output of the print statement in python.
        """
        while(num>0):
            self.rem = num%10
            print(self.rem,end="")
            num //= 10

val = int(input("Enter a number to reverse: "))
sol = Reverse()
sol.printReverse(val)

