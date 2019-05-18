#def finder(lis1, lis2):
#    def find2(li_1,li_2):
#        for num in li_1:
#            if num not in li_2:
#                print(num)
#    if len(lis1)>len(lis2):
#        find2(lis1, lis2)
#    elif len(lis1)<len(lis2):
#        find2(lis2, lis1)
#
#finder([1,2,3,4,6,7],[1,2,3,4,6])

#def finder(arr1, arr2):
#    arr1.sort()
#    print(arr1)
#    arr2.sort()
#    print(arr2)
#    for num1, num2 in zip(arr1,arr2):
#        if num1 != num2:
#            return num1
#    print(arr1[-1])
'''
import collections
def finder2(arr1, arr2): 
    
    # Using default dict to avoid key errors
    d=collections.defaultdict(int) 
    
    # Add a count for every instance in Array 1
    for num in arr1:
        d[num]+=1 
    print(d)
    # Check if num not in dictionary
    for num in arr2: 
        if d[num]==0: 
            print(num)
        
        # Otherwise, subtract a count
        else: 
            d[num]-=1
            print(d)
finder2([1,2,4,3],[1,2,3,4,5]) 
'''

def sorty(a):
    length =len(a)-1
    for k in range(0,length):
        for l in range(0,length-k):
            if a[l]>a[l+1]:
                a[l],a[l+1]=a[l+1],a[l]
                

def miss(a1,a2):
    