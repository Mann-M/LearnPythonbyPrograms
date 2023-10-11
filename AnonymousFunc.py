print('Program to Display power of two using Anonymous Function\n')

#lamda function

nterms= int(input("enter the no of terms here\n"))
result=list(map(lambda x: 2**x, range(nterms+1)))

print(result)
