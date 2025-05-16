#Using for
f=1
num=int(input('enter num='))
for i in range(num,0,-1):
    f=f*i
print(f)


#Using while 
num = int(input("Num= "))

f = 1
i = 1
while i <=num:
    i+=1
    f =f*i
    print(f)


#Formatting
num = int(input("Num ="))
i = 0
f = 1
while i <num:
    i+=1
    f =num*i
    print(num,"*",i,"=",f)
