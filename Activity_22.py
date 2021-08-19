def main():
   x=number()
   import math
   r=x*22/(180*7)
   sum=0
   for i in range(0,85,1):
      sum = sum + (pow(-1,i))*pow(r,(2*i+1))/(math.factorial(2*i+1))
   
   print(sum)
def number():
   x=int(input("Enter the angle in degrees - "))
   return x
main()

