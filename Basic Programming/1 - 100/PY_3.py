class OddNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def printOddNumbers(self):
        print("Odd Numbers in Given Range: ")
        for i  in range(self.start, self.end+1):
            if (i%2==1):
                print(i)

start = int(input("Enter the lower limit for the range: "))
end = int(input("Enter the upper limit for the range: "))

Soln = OddNumbers(start, end)
Soln.printOddNumbers()