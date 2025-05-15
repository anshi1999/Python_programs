#Using for 
num=int(input('enter num='))
i=2
for i in range(i,num):
    if num%i==0:
        print('not prime')
        break
else:
    print('prime')

# Using while notes its increment code position

num=int(input('enter num='))
i=2
while i<num:
    if num%i==0:
        print('not prime')
        break
    i+=1
else:
    print('prime')
