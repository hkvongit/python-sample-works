
# INPUT ARRAY MUST BE ORDERED

def ordered_seq_search(lis, target):
    for ele in lis:
        if ele<=target:
            print(ele)
            if ele == target:
                index= lis.index(ele)
                return index
        else:
            return False
        

lis=[5,4,6,9,10]
result=ordered_seq_search(lis,8)
if result!=False:
    print(f'found at {result+1}')
else:
    print('not found')
    