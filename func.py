#def add_sub(a,b):
#    c=a+b
#    d=a-b
#    return c,d
#print(add_sub(8,6))

#def aa(name='hari'):
#    print(name)
#
#aa('sri')

#def key(name, roll):
#    print(name,roll)
#
#key(name='hari', roll=10)

#def hh(*args):
#    print(*args)
#
#hh('haru','sri',10)

#a=10
#
#def aa():
#    a=15
#    x=globals()['a']
#    print(id(x),x)
#    print(id(a),a)
#
#aa()
#print(id(a),a)


#li=[1,2,3,4,5,6,7]
#def oddoreven(lis):
#    o=' '
#    e=' '
#    for i in lis:
#        if i%2==0:
#            e=e+' '+str(i)
#        else:
#            o=o+' '+str(i)
#    print(f'the odd numbers are {o}')
#    print(f'the even numbers are {e}')
#
#oddoreven(li)

##li=[1,2,5,4,8,6,7]
##def oddoreven(lis):
##    o=' '
##    e=' '
##    for i in range(len(lis)):
##        if lis[i]%2==0:
##            e=e+' '+str(i)
##        else:
##            o=o+' '+str(i)
##    print(f'the odd numbers are {o}')
##    print(f'the even numbers are {e}')
##
##oddoreven(li)


#num=5
#c=1
#def fac(num):
#    p=1
#    for i in range(1,num+1):
#        p=p*i
#    print(p)    
#fac(num)
#
#def fa(n):
#    if n>0:
#        fac=n*fa(n-1)
#        return fac
#    else:
#        fac=1
#        return fac
#
#print(fa(6))

from functools import reduce

lis=[1,2,5,8,6,3,4]
addup =reduce(lambda a,b:a+b, lis)

print(addup)

#evens=list(filter(lambda n:n%2==0,lis))
#
#doubles= list(map(lambda n:n*2, lis))
#even_doubles= list(map(lambda n:n*2, evens))
#print(doubles)
#print(evens)
#print(even_doubles)


