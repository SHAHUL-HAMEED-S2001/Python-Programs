# Python Program to find the binary equivalent of a number using Recursion

class Program:
    def __init__(self):
        self.binary=[]

    def binaryEquivalent(self,val):
        if(val==0):
            soln.printBinaryEquivalent()
            return
        self.binary.append(val%2)
        soln.binaryEquivalent(val//2)

    def printBinaryEquivalent(self):
        self.binary.reverse()
        print("Binary Equivalent of Given Number is ",end="")
        i = 0
        while(i<len(self.binary)):
            print(self.binary[i],end="")
            i=i+1

num = int(input("Enter a number: "))
soln = Program()
soln.binaryEquivalent(num)

            
