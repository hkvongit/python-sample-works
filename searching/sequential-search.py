def ss(lis,target):
    i=0
    while i<len(lis):
        if lis[i]==target:
            return i
        else:
            i+=1
    return False


lis=[5,4,6,2,7]
result=ss(lis,6)
if result!=False:
    print(f'found at {result+1}')
else:
    print('not found')
    
