print("\nProgram to print multiplication table of any number to any limit\n")
print('using for loop\n')

num=int(input('Enter the number you want the multiplication table of:\n'))
limit=int(input('Enter to where you want the table to(from 1)\n'))
print("The multiplication table of",num,"is:-\n")
for i in range(1,limit+1):
    print(num,'X',i,'=',num*i)

print('using while loop\n')
i=1
print("The multiplication table of",num,"is:-\n")

while i<=limit:
    print(num,'X',i,'=',num*i)
    i=i+1
