class Deque(object):
    def __init__(self):
        self.items=[]
    def addFront(self,item):
        return self.items.append(item) 
    def addRear(self, item):
        return self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        print(len(self.items))
    
x=Deque()
x.addFront('sha')
x.addRear('xx')
print(x.size())
print(x.items)
x.removeFront()  
print(x.items)