# Python Program to Print All Odd Numbers in a Range
class Program:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def printOddNumbers(self):
        print("Odd Numbers in Given Range: ")
        for i  in range(self.start, self.end+1):
            if (i%2==1):
                print(i)

print("Python Program to Print All Odd Numbers in a Range")

start = int(input("Enter the lower limit: "))
end = int(input("Enter the upper limit: "))

Soln = Program(start, end)
Soln.printOddNumbers()