# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3
class Program:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def printNumbers(self):

        for i in range(self.start,self.end+1):
            if((i%2 != 0) & (i%3 != 0)): print(i)

start = int(input("Enter the lower limit for the range: "))
end = int(input("Enter the upper limit for the range: "))

soln = Program(start, end)
print("All Integers that Aren’t Divisible by Either 2 or 3")
soln.printNumbers()