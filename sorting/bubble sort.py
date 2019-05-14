def bubble_sort(lis):
    length=len(lis)-1
    for i in range(0,length):
        for j in range(0,length-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis
            
lis=[3,6,9,2,1,10,5]
print(bubble_sort(lis))