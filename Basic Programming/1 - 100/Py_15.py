# Python Program to find the binary equivalent of a number

class Program:
    def binaryEquivalent(self,val):
        binary =  []
        while(val>0):
            binary.append(val%2)
            val//=2
        binary.reverse()
        print("Binary Equivalent of Given Number is ",end="")
        i = 0
        while(i<len(binary)):
            print(binary[i],end="")
            i=i+1

num = int(input("Enter a number: "))
soln = Program()
soln.binaryEquivalent(num)
            
