# Python Program to count the number of digits in a number

class Program:
    def printReverse(self,val):
        print("Reverse of a Given Number is ",end="")
        while val>0:
            print( val % 10, end="")
            val//=10

num = int(input("Enter a number: "))
soln = Program()
soln.printReverse(num)