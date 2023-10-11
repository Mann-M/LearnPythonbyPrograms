print("\nProgram to print all the armstrong no.s in a given interval\n")
start=int(input('Enter the start:\n'))
end=int(input('Enter the end:\n'))
armstrong_list=[]
for i in range(start,end+1):
    length=len(str(i))
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        cube=digit**length
        sum=sum+cube
        temp=temp//10
    if i==sum:
#         print(i)
        armstrong_list.append(i)

print(armstrong_list)