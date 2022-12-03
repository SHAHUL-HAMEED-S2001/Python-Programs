# Python Program to take in the marks of 5 subjects and display the grade

class Program:
    """    def __init__(self):
        self.subject1=0
        self.subject2=0
        self.subject3=0
        self.subject4=0
        self.subject5=0"""

    def getMarks(self):
        self.subject1=int(input(" Enter Subject 1 Mark: "))
        self.subject2=int(input(" Enter Subject 2 Mark: "))
        self.subject3=int(input(" Enter Subject 3 Mark: "))
        self.subject4=int(input(" Enter Subject 4 Mark: "))
        self.subject5=int(input(" Enter Subject 5 Mark: "))

    def printGrade(self):
        self.average= (self.subject1 + self.subject2 + self.subject3 + self.subject4 + self.subject5)/5
        if(self.average>=90):
            print("Grade: A")
        elif(self.average>=80 & self.average<90):
            print("Grade: B")
        elif(self.average>=70& self.average<80):
            print("Grade: C")
        elif(self.average >=60 & self.average<70):
            print("Grade: D")
        else:
            print("Grade: F")

soln = Program()
soln.getMarks()
soln.printGrade()