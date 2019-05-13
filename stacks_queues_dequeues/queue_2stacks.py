def sq(lis):
    lis2=[]
    length = len(lis)
    for l in lis:
        for i in range(length):
            lis2[i]=lis.pop(l)

