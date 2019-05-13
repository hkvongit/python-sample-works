def fact(num):
    if num ==0:
        return 1
    else:
        result = num*fact(num-1)
        return result



     

print(fact(10))