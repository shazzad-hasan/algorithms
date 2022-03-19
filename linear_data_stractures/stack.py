class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self): # tests to see whether the stack is empty
        return self.items == []

    def size(self): # returns the number of items on the stack
        return len(self.items)
    
    def push(self, item): # adds a new item to the top, returns nothing
        self.items.append(item)
        
    def peak(self): # returns the top item
        return self.items[len(self.items)-1]
        
    def pop(self): # removes the top item, stack gets modified.
        return self.items.pop()
    

item_list = ['cat', 10, 'dog'] 
   
s = Stack()
print(s.isEmpty())
for e in item_list:
    s.push(e)
print(s.isEmpty())
print(s.size())
print(s.peak())
s.pop()
print(s.peak())
s.push(False)
print(s.peak())
while not s.isEmpty():
    s.pop()
print(s.isEmpty())
print(s.size())