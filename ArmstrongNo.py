print('\nProgram to check if the number is Armstrong Number\n')

num=int(input('Enter a number\n'))
sum=0
temp=num
length=len(str(temp))
    

while temp>0:
    
    digit=temp%10
    #print(digit)
    cube=digit**length
    #print(cube)
    sum=sum+cube
    #print(sum)
    
    temp=temp//10
    #print(temp)
    
if sum==num:
    print(num,'is an Armstrong Number')
else:
    print(num,'is not an Armstrong Number')
