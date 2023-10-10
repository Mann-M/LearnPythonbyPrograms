# Program to chech if the year is a leap year or not
# for  centuary year num%400==0 and num%100==0
# for non centuary year num%4==0 and num%100!=1

year=int(input("\nEnter a year:\n"))

if (year%400==0) and (year%100==0):
    print(year,"is leap year centuary")
elif (year%4==0) and (year%100 !=0):
    print(year,"is a leap year ")
else:
    print(year,"is not a leap year")