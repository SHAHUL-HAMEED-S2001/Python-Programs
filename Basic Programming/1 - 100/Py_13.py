# Python Program to generate all the divisors of an integer

class Program:
    def printDivisors(self,val):
        print("Divisors of Given Number:")
        for i in range(1,val+1):
            if(val%i==0): print(i)

num = int(input("Enter a number: "))
soln = Program()
soln.printDivisors(num)