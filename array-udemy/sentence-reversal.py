#def rv(sen):
#    lis=sen.split()
#    print(lis)
#    lis.reverse()     
#    print(lis)
#    can=''
#    for se in lis:
#        can+=se+' '
#    print(can)
#
#sen='  there are good peoples too  '
#rv(sen)
def rv2(sentence):
    lis=[]
    word=''
    sentence+=' '
    space=' '
    l=0
    length =len(sentence)
    print(length)
    for l in range(length):
        if sentence[l] !=space:
            word+=sentence[l]
            print(word)
        elif (sentence[l]==space):
            lis.append(word)
            print(l)
            word='' 
    print(lis)
    print(' '.join(reversed(lis)))



sentence="hi this is summer la"
#print(sentence[])
rv2(sentence)
'''
def rev_word3(s):
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    print(" ".join(reversed(words)))
s='hi this is hkv  '
rev_word3(s)
'''