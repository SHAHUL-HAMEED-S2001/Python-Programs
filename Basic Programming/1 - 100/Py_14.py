# Python Program to find the smallest divisor of an integer

class Program:
    def smallDivisor(self,val):
        for i in range(2,val+1):
            if val%i==0: return i

num = int(input("Enter a number: "))    
soln = Program()
print("Small Divisor of Given Number is",soln.smallDivisor(num))