
class Program:
    def isPositive(self,val):
        if(val>0): return 0
        else:   return 1

num = int(input("Enter a number: "))
soln = Program()
if(soln.isPositive(num)): print("Entered Number is Positive")
else:   print("Entered Number is Negative")