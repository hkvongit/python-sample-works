#i=0
#s=0
#def cha():
#    for i in range(3):
#        s=int(input('enter is    : '))
#        for c in range(s):
#            print('#', end='')
#        print('\n')
#        
#
#            
#cha()
a=[]
def app():
    for i in range(0,3):
        score=int(input('enter your score   :'))
        a.append(score)
        
    for e in a:
        print('#'*e)

app()
        