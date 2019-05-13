# a="i am   fine "
# s=a.split(' ')
# sep=''
# k=s[::-1]
# q=sep.join(k)
# print(s)
# print(k)
# for i in k:
#     print(i,end =" ") 



def bst(k,f,l,target):
    if l>=f:
        mid=(f+l)//2
        if target == k[mid]:
            return mid
        elif target>k[mid]:
            f=mid+1
            return bst(k,f,l,target)
        elif target<k[mid]:
            l=mid-1
            return bst(k,f,l,target)
    else: 
        return False


le=[56,23,8,12,9]
k=sorted(le)
print(k)
length =len(k)-1

result=bst(k,0,length,9)
if result!=False:
    print(f'found at {result}')
else:
    print('not found')
    

