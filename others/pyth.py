'''av=5
need=int(input('how much you need : '))
i=1
while (i<need):
    if i>av:
        print('out of stock')
        break
    print('candy',i)
    i+=1
print('finished')
'''

for i in range(1,51):
    if (i%2==0):
        if (i%3==0):
            continue
        else:
            print(i)