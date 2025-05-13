#POSITIVE AND NEGATIVE
#BRUTE FORCE 
num = int(input("Num= "))
if num ==0:
    print("Zero")
elif num >=0:
    print("positive")
else:
    print("negative")


#NESTED IF-ELSE
num = int(input("Num= "))
if num>=0:
    if num !=0:
        print("positive")
    else:
        print("Zero")
else:
    print("negative")


#TERNARY APPROACH
num = int(input("Num= "))
print("positive" if num>=0 else "negative")
