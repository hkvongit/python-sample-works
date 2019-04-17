import sys

lis= []

n=10

for i in range(n):
    a=len(lis)
    b=sys.getsizeof(lis)
    print(lis)
    print(f'length: {a} size in bytes  : {b}')
    lis.append(n)
    



    