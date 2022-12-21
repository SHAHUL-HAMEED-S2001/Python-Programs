# Python Program to Print All Numbers in a Range Divisible by a Given Number

class Program:
    def __init__(self,start,end,div):
        self.start = start
        self.end = end
        self.div = div

    def printNumbers(self):
        print("Numbers which are Divisible by",self.div,"in a Given Range:-")
        for i in range(self.start,self.end+1):
            if((i%self.div == 0)): print(i)

print("Python Program to Print All Numbers in a Range Divisible by a Given Number")

start = int(input("Enter the lower limit for the range: "))
end = int(input("Enter the upper limit for the range: "))
div = int(input("Enter the number to be divided by: "))

Soln = Program(start, end, div)
Soln.printNumbers()