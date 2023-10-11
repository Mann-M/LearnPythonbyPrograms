print('\nProgram to print all Prime numbers in a range/interval\n')

initial=int(input("Enter inital number\n"))
end=int(input("Enter end number\n"))

prime_numbers =[]

for num in range(initial,end):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_numbers.append(num)

print("list of prime no.s between",initial,"and",end,"are\n",prime_numbers)