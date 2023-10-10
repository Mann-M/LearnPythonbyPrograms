# By using exponentiation
print("\nBy using exponentiation ie square = num to the power of half ")
num = int(input("enter number: "))
sr = num**(1/2)  #square = num to the power of half

print("the square root of",num, "is",sr)

# By using math module

print("\nBy using Math module in Python")

import math
sr_mm=math.sqrt(num)

print("the square root of",num,"is",sr_mm)
