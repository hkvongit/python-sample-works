def sc(word):
    strcom=''
    counter=1
    word=word+' '
    for l in range(1,len(word)):
        if word[l]==word[l-1]:
            counter+=1
        elif word[l]!=word[l-1]:
            strcom+=word[l-1]+str(counter)
            counter=1
    print(strcom)

sc('haaRIIi')

