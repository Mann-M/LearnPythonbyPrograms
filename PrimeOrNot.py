# Program to check if the no. is prime or not
#prime no is the no. that is divisible by itself and one only


print('\nCheck if the no is a Prime Number\n')
num=int(input('Enter a number:\n'))

if num==1:
    print(num,'is not a prime number\n')
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,'is not a prime number\n')
            break
else:
    print(num,'is a prime number')
