print('fibonacci series print')

limit=int(input('Enter a number to where you want the series to:\n'))

a=0
b=1
fibonacci_series=[0,1,]
for i in range(2,limit):
    c=a+b
    a,b=b,c
    fibonacci_series.append(c)
    
print(fibonacci_series)
    