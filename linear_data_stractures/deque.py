class Deque(object):
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item): # adds a new item to the front
        self.items.append(item)
        
    def addRear(self, item): # adds a new item to the rear
        self.items.insert(0, item)
        
    def removeFront(self): # removes the front item
        return self.items.pop()
    
    def removeRear(self): # removes the rear item
        return self.items.pop(0)
    
d = Deque()
print(d.isEmpty())
print(d.size())

d.addFront('x')
d.addRear('y')
print(d.isEmpty())
print(d.size())

d.removeFront()
d.removeRear()
print(d.isEmpty())
print(d.size())