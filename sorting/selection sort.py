def selection_sort(lis):
    length = len(lis)-1
    for posi in range(length, 1,-1):
        posOfMax=posi
        for ite in range(0,posi):
            if lis[ite]>lis[posOfMax]:
                #print(f' ite is{lis[ite]}: posOfMax is  {lis[posOfMax]}')
                posOfMax=ite
                #print(f'posOfMax is {lis[posOfMax]}')
        temp=lis[posi]
        lis[posi]=lis[posOfMax]
        lis[posOfMax]=temp
        #print(f'lis[posi],lis[posOfMax]={lis[posOfMax],lis[posi]')
        print(lis)
    return lis

lis=[33,2,9,8,18,55,13,1]
r=selection_sort(lis)
print(r)
