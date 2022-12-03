# Python Program to read height in centimeters and then convert the height to feet and inches

class Program:
    def convertToInches(self,val):
        return round(val*0.394,2)

    def convertToFeet(self,val):
        return round(val*0.0328,2)

num =int(input("Enter the height in centimeters: "))

soln = Program()
print("The length in inches",soln.convertToInches(num))
print("The length in feet",soln.convertToFeet(num))