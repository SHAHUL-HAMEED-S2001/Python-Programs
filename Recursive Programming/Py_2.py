# Python Program to Check if a Number is a Palindrome using Recursion

class Program:
    def __init__(self):
        self.dup = 0
        
    def checkPalindrome(self,num):
        if num == 0:
            return
        
        self.dup = self.dup*10 + (num%10)  
              
        sol.checkPalindrome(num//10)
    
    def isPalindrome(self,num):
        sol.checkPalindrome(num)
        if (num == self.dup): return 1
        else: return 0

val = int(input("Enter number to check for Palindrome: "))
sol = Program()

if (sol.isPalindrome(val)):
    print("Entered number is Palindrome")
else:
    print("Entered number is not a Palindrome")