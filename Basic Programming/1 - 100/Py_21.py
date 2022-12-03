# Python Program to read a number n and compute n+nn+nnn

class Program:
    def compute(self,val):
        temp=str(val)
        t1=temp+temp
        t2=temp+temp+temp
        comp=val+int(t1)+int(t2)
        print("The value of",val,"+",t1,"+",t2,"is",comp)

num = int(input("Enter a number n: "))

soln=Program()
soln.compute(num)