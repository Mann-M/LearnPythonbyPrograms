# Program to find the largest number

num1=float(input("Enter 1st no. :\n"))
num2=float(input("Enter 2nd no. :\n"))
num3=float(input("Enter 3rd no. :\n"))

if (num1>num2) and (num1>num3):
    print(num1,"is the largest")
elif(num2>num1) and (num2>num3):
    print(num2,"is the largest")
else:
    print(num3,"is the largest")