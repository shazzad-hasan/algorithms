class Array:
    def __init__(self): # O(1)            
        self.A = []
        self.size = 0
        
    def __len__(self): # O(1)
        return self.size 
    
    def __iter__(self): # O(n)
        yield from self.A
        
    def build(self, items): # O(n)
        self.A = [a for a in items] 
        self.size = len(self.A)
        
    def get_at(self, i): # O(1)
        return self.A[i]
    
    def set_at(self, i, item): # O(1)
        self.A[i] = item
        
    def copy_forward(self, i, n, A, j): # O(n)
        for k in range(n):
            A[j+k] = self.A[i+k]
    
    def copy_backward(self, i, n, A, j): # O(n)
        for k in range(n-1, -1, -1):
            A[j+k] = self.A[i+k]
            
    def insert_at(self, i, item):
        n = len(self)
        A = [None] * (n+1)
        self.copy_forward(0, i, A, 0)
        A[i] = item
        self.copy_forward(i, n-i, A, i+1)
        self.build(A)
        
    def delete_at(self, i):
        n = len(self)
        A = [None] * (n-1)
        self.copy_forward(0, i, A, 0)
        item = self.A[i]
        self.copy_forward(i+1, n-i-1, A, i)
        self.build(A)
        return item 
        
    def insert_first(self, item):
        self.insert_at(0, item)
        
    def insert_last(self, item):
        self.insert_at(len(self), item)
        
    def delete_first(self):
        return self.delete_at(0) 
        
    def delete_last(self):
        return self.delete_at(len(self)-1)
        
        
my_array = Array()

L = [31, 77, "hello", 54, "world"]
my_array.build(L)


for e in my_array:
    print(e)

my_array.set_at(2, 'cat')
print()
print(my_array.get_at(2))

my_array.insert_at(3, 'Jon')
print(my_array.get_at(3))

my_array.delete_at(3)
print(my_array.get_at(3))

my_array.insert_first(0)
my_array.insert_last('dog')
print()
for e in my_array:
    print(e)
    
my_array.delete_first()
my_array.delete_last()
print()
for e in my_array:
    print(e)



