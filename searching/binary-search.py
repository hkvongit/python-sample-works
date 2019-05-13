
''' we can use both recursion and iteration to find solution'''

# BINARY SEARCH USING RECURSION

def binary_search(lis, f, l, target):
    mid=int((l+f)/2)
    if l>=f:
        if lis[mid]==target:
            return mid
        elif lis[mid]>target:
            l=mid-1
            return binary_search(lis, f, l, target)
        else:
            f=mid+1
            return binary_search(lis, f, l, target)
    else:
        return -1

lis=[2,5,6,9,10,12,14,15,16,17,18,111]
result=binary_search(lis, 0, len(lis)-1, 2)
if result!=-1:
    print(f'found at {result+1}')
else:
    print('not found')


# BINARY SEARCH USING ITERATION

def bin_se_ite(lis,f,l,target):
    while f<=l:
        mid=(l+f)//2
        if lis[mid]==target:
            return mid
        elif lis[mid]>target:
            l=mid-1
        else:
            f=mid+1
    else:
        return -1

lis=[2,5,6,9,10,12,14,15,16,17,18,111]
result=bin_se_ite(lis, 0, len(lis)-1, 111)
if result!=-1:
    print(f'found at {result+1}')
else:
    print('not found')


