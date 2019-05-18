num_int=int(input('please enter a number    :'))
rev_bin=''
print(bin(num_int))
while num_int>0:
    if num_int %2==0:
        num_int=int(num_int/2)
        rem=0
        rev_bin=rev_bin+str(rem)
        
    elif num_int %2==1:
        num_int=int(num_int/2)
        rem=1
        rev_bin=rev_bin+str(rem)

bina=rev_bin[::-1]
print('the binary format is     :')
print(bina)     