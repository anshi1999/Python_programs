# Even from 1 to 100
i = 0
while i<=100:
    if i%2 ==0:
        print(i)
    i+=1


#Odd from 1 to 100
i = 0
while i<=100:
    if i%2 !=0:
        print(i)
    i+=1


#Even from 100 to 1
i = 100
while i>=0:
    if i%2 ==0:
        print(i)
    i-=1

#Odd from 100 to 1
i = 100
while i>=0:
    if i%2 !=0:
        print(i)
    i-=1



#Using for 
for i in range(1,101):
    if i%2==0:
        print(i,'even')
    else:
        print(i,'odd')


#Reverse
for i in range(100,0,-1):
    if i%2==0:
        print(i,'even')
    else:
        print(i,'odd')
