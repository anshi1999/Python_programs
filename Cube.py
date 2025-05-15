#Using for short 
num=int(input('enter num='))
for i in range(1,num+1):
    print(i,i**3)


# Using While
num=int(input('enter num='))
i = 1
c = 1
while i <=num:
    cb = i**3
    i+=1
    print(i,cb)
