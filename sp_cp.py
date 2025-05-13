cp=float(input('enter cost price='))
sp=float(input('enter selling price='))
if sp>cp:
    print('profit')
elif sp<cp:
    print('loss')
else:
    print('no profit or loss')
