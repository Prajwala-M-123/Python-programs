def computeGCD(x,y):
 if x>y:
  smaller=y
 else:
  smaller=x
 for i in range(1, smaller+1):
  if (x % i==0) and (y %i ==0):
   gcd=i
 return gcd
# Example usage:
#num1 = 54:
#num2 = 24:
#Take input from the user
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("The GCD of", num1, "and", num2, "is", computeGCD(num1,num2))   
