def sorty(li):
    for j in range(0,len(li)-1):
        for i in range(0,len(li)-j-1):
            if li[i]>li[i+1]:
                li[i], li[i+1]= li[i+1], li[i]
               


li=[5,2,6,3,4,7,88,44]
sorty(li)
print(li)


# li=[5,4,2,3]
# for j in range(0,3):
#     for i in range(0,3):
#         if li[i]>li[i+1]:
#             li[i], li[i+1]= li[i+1], li[i]
# print(li)