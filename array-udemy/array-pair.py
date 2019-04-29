
def pai(arr, k):
    arra=set()
    arrb=set()
    for num in arr:
        target = k - num
        if target not in arra:
            arra.add(num)
        else:
            arrb.add((max(num,target),min(num,target)))

    print(arrb)

pai([1,3,2,2],4)

