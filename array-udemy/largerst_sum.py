'''#my solution

def summo(arr):
    sum_a=0
    sum_list=[]
    for num in arr:
        sum_a+=num
        sum_list.append(sum_a)
    sum_list.sort()
    print(sum_list[len(sum_list)-1])

summo([1,2,-1,3,4,10,10,-10-1])
'''
#I dont know the below logic is right or not
'''
def large_conti_sum(arr):
    if len(arr)==0:
        print('there are no elements')
    else:
        max_sum=current_sum=arr[0]
        for num in arr[1:]:
            current_sum=max(current_sum+num,num)
            max_sum=max(max_sum, current_sum)
        print(max_sum)

large_conti_sum([1,2,-1,3,4,-10,10,-10,-1])
'''