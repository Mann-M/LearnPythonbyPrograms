print("\nFactorial of the number\n")
print('using for loop-\n')
num=int(input('Enter a number\n'))

fact=1

if num<0:
    print("factorial of 0 does not exist\n")
elif num==0:
    print('factorial of 0 is 1\n')
elif num>0:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of",num,"is\n",fact)

print('\nusing recursion\n')

def fact(a):
    if a==0:
        return 1
    
    else:
        return (a*fact(a-1))
    
print("factorial of",num,"is-",fact(num))