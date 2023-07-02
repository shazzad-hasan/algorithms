class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self): # tests to see whether the queue is empty
        return self.items == []
    
    def size(self): # returns the number of items
        return len(self.items)
    
    def enqueue(self, item): # O(1), adds a new item to the rear
        self.items.insert(0, item)
        
    def dequeue(self): # O(n), removes the front item, queue gets modified.
        return self.items.pop()
    
if __name__=="__main__":

    q = Queue()
    
    print(q.is_empty())
    print(q.size())

    L = ['x', 'y', 'z', 'xyz', 1, 2]
    for l in L:
        q.enqueue(l)

    print(q.is_empty())
    print(q.size())
    print(q.dequeue())
    print(q.size())

    while not q.is_empty():
        q.dequeue()
    print(q.size())
    