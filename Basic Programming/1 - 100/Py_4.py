# Python Program to Check if a Number is a Palindrome
class Program:
    def __init__(self):
        self.rem = 0
        self.add = 0
        self.dup = 0

    def isPalindrome(self,num):
        self.dup = num
        while(num>0):
            self.rem = num%10
            self.add = self.add*10 + self.rem
            num //= 10
       
        return (self.dup == self.add)

val = int(input("Enter number to check for Palindrome: "))
sol = Program()

if (sol.isPalindrome(val)):
    print("Entered number is Palindrome")
else:
    print("Entered number is not a Palindrome")