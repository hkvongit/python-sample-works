
def divi(lis):
    for i in lis:
        if i%5==0:
            print(i)
            break
    else:
        print('not found')

li=[1,2,3,4,6,7,8,9]
divi(li)

lis=[1,5,10,15]
divi(lis)