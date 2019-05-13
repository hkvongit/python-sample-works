def ds(num):
    if num <10:
        return num
    else:
        return (num%10)+ds(int(num/10))

print(ds(5672))