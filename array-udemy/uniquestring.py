

def uni(word):
    a=set()
    for letter in word:
        if letter in a:
            return False
        else:
            a.add(letter)

word="hai"
uni(word)
if uni(word) is False:
    print('not unique')
else:
    print('unique')