def bracket(art):
    opening_brackets = ['{','[','(']
    pair= [('[',']'),('{','}'),('(',')')]
    stack=[]
    if len(art)%2!=0 or len(art)==0 :
        return False
    else:
        for l in art:
            if l in opening_brackets:
                stack.append(l)
            else:
                popped = stack.pop()
                if (popped,l) not in pair:
                    return False

        
    
a='{()[]}'
if bracket(a) is False:
    print(" not closed correctly")
else:
    print('closed correctly')
