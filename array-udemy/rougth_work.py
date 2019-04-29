def uni(word):
    cu=[]
    for l in word:
        if l in cu:
            return False
        else:
            cu.append(l)
    return True

word='buha'
if uni(word):
    print('unique')
else:
    print('not unique')