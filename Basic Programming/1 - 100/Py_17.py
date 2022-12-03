# Python Program to print the table of a given number

class Program:
    def printTable(self,val):
        for i in range(1,11):
            print(i,"x",val,"=",i*val)

num = int(input("Enter a number: "))

soln = Program()
soln.printTable(num)