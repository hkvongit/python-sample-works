class Dll(object):
    def __init__(self, value):
        self.value=value
        self.prev_node=None
        self.next_node=None 

a=Dll(1)
b=Dll(2)
c=Dll(3)

a.next_node=b
b.prev_node=a
b.next_node=c
c.prev_node=b

print(a.next_node.next_node.value)