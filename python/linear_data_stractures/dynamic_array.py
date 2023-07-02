class Dynamic_Array:
    def __init__(self, r=2):                # O(1)
        self.A = []
        self.size = 0
        self.r = r 
        self._compute_bounds()
        self._resize(0)

    def __len(self):                        # O(1)
        return self.size 

    def __iter__(self):                     # O(n)
        yield from self.A
             
    def build(self, X):                     # O(n)
        for a in X:
            self.insert_last(a)
        self.size = len(self.A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):                 # O(1)
        self.A[i] = x 

    def _copy_forward(self, i, n, A, j):    # O(n)
        for k in range(n):
            A[j+k] = self.A[i+k]

    def _copy_backward(self, i, n, A, j):   # O(n)
        for k in range(n-1, -1, -1):
            A[j+k] = self.A[i+k]

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):                   # O(1) or O(n)
        if self.lower < n < self.upper:
            return 
        m = max(n, 1) * self.r 
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A 
        self._compute_bounds()

    def insert_last(self, x):               # O(1)a
        self._resize(self.size + 1)
        self.A[self.size] = x 
        self.size += 1 

    def delete_last(self):                  # O(1)a
        self.A[self.size - 1] = None 
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):
        self.insert_last(None)
        self._copy_backward(i, self.size-(i+1), self.A, i+1)
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self._copy_forward(i+1, self.size-(i+1), self.A, i)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

if __name__=="__main__":
    my_array = Dynamic_Array()
    L = [31, 77, "hello", 54, "world"]
    my_array.build(L)


    for e in my_array:
        print(e)

    my_array.set_at(2, 'cat')
    print()
    for e in my_array:
        print(e)

    my_array.insert_at(3, 'Jon')
    print()
    for e in my_array:
        print(e)

    my_array.delete_at(3)
    print()
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
