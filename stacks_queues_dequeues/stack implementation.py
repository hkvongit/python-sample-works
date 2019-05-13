class Stack(object):
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        print(self.items[len(self.items)-1])
    def isEmpty(self):
        if len(self.items)==0:
            print("empty")
        else:
            print('not empty')
    def size(self):
        print(len(self.items))

x=Stack()
x.isEmpty()
x.push('dad')
x.peek()
x.size()