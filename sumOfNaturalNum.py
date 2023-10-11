print('\nPrint the sum of natural number to the given number\n')

num=int(input('Enter a number\n'))

if num<0:
    print('Enter a nuatural number\n')

else:
    sum=0
    while num>0:
        sum+=num
        num-=1
print(sum)