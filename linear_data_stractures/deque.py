class Deque:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item): # adds a new item to the front
        self.items.append(item)
        
    def add_rear(self, item): # adds a new item to the rear
        self.items.insert(0, item)
        
    def remove_front(self): # removes the front item
        return self.items.pop()
    
    def remove_rear(self): # removes the rear item
        return self.items.pop(0)
    
d = Deque()
print(d.is_empty())
print(d.size())

d.add_front('x')
d.add_rear('y')
print(d.is_empty())
print(d.size())

d.remove_front()
d.remove_rear()
print(d.is_empty())
print(d.size())