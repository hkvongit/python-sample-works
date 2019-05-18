num=25
print(bin(num))
rev_bi=''
while(num>0):
    if num%2==0:
        rem='0'
        rev_bi+=rem
    elif (num%2==1):
        rem='1'
        rev_bi+=rem
    num=num//2

print(rev_bi[::-1])
