# By using third variable

x=10
y=20
print("initial value of x=",x, "& y=",y)
temp=x
x=y
y=temp

print("x=",x,"y=",y)

# without using third variable
x=10
y=20
x,y=y,x

print("the vales of x and y are:",x,y)