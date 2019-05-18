def insertion_sort(lis):
    length =len(lis)-1
    for i in range(1,length+1):
        backy=i # this will help to move the correct position of the inserting the i-th element 
        current=lis[i] # a alternate storage for the i-th element
        for j in range(i,0,-1):
            if current<lis[j-1]:
                lis[j]=lis[j-1]
                '''for every forward insertion of the lis elements 
                we need to find the right position to insert our foremost i-th element'''
                backy-=1  
                print(backy,lis[backy])
        lis[backy]=current
        print(lis)
    return lis

lis=[2,9,6,7,5,11,1]
print(insertion_sort(lis))