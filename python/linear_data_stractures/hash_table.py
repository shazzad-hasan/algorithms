class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size 
        self.data = [None] * self.size 

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key 
            self.data[hash_value] = data 

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data 
            else:
                next_slot = self.rehash(hash_value, len(self.slots))

                while (self.slots[next_slot] is not None and self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots)) 

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key 
                    self.data[next_slot] = data 
                else:
                    self.data[next_slot] = data 


    def hash_function(self, key, size):
        return key % size 

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size 

    def get(self, key):
        start = self.hash_function(key, len(self.slots)) 

        current = start
        while self.slots[current] is not None:
            if self.slots[current] == key:
                return self.data[current]
            else:
                current = self.rehash(current, len(self.slots))
                if current == start:
                    return None 

    def __getitem__(self, key):
        return self.get(key) 

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__=="__main__":
    h = HashTable()
    h[20] = "horse"
    h[26] = "cat"
    h[33] = "lion"
    h[8] = "tiger"
    h[0] = "bird"
    h[11] = "cow"
    h[44] = "bear"
    h[55] = "elephant"
    h[25] = "chicken"

    for i in range(h.size):
        print("{} -- > {}".format(h.slots[i], h.data[i])) 

    print(h.slots)
    print(h.data)

    print(h[25])
    h[20] = "duck"
    print(h[20])

   


