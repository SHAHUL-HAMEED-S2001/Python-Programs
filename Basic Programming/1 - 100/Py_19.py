# Python Program to check whether a given year is a leap year or not

class Program:
    def checkIsLeapYear(self,val):
        if(val%4==0 and val%100!=0 or val%400==0): return 1
        else: return 0

num = int(input("Enter year to check Leap Year: "))
soln = Program()

if(soln.checkIsLeapYear(num)): print("Entered year is Leap Year")
else: print("Entered year is not a Leap Year")