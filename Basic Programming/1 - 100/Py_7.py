# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

class Program:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def printNumbers(self):
        print("Numbers which are Divisible by 7 and Multiple of 5 in a Given Range:-")
        for i in range(self.start,self.end+1):
            if((i%7 == 0) & (i%5 == 0)): print(i)

start = int(input("Enter the lower limit for the range: "))
end = int(input("Enter the upper limit for the range: "))

Soln = Program(start, end)
Soln.printNumbers()