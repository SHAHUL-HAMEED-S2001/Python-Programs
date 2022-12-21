# Python Program to Reverse a Number using Recursion

class Program:
    def printReverse(self,num):
        if num == 0:
            return 
        print(num%10,end="")
        sol.printReverse(num//10)

val = int(input("Enter a number to reverse: "))
sol = Program()
print("Reversed Number of",val,"is ",end="")
sol.printReverse(val)

"""
Note:
The end parameter in the print function is used to add any string. 
At the end of the output of the print statement in python.
"""
