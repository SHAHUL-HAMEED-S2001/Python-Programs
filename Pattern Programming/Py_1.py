# Floyd's triangle

class Program:
    
    def printFloydTriangle(self,num):
        count = 1
        col = 0
        for row in range(num):
            for col in range(row+1):
                print(count)
                count+=1
        
val = int(input("Enter number of Rows to Print Floyd's triangle: "))
sol = Program()
sol.printFloydTriangle(val)