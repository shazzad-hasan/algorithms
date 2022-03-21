class StaticArray:
    def __init__(self, n):
        self.data = [None] * n
        
    def get_at(self, i):                           # O(1)
        if (i < 0 or i > len(self.data)):
            raise IndexError
        return self.data[i]
    
    def set_at(self, i, x):                        # O(1)
        if (i < 0 or i > len(self.data)):
            raise IndexError
        self.data[i] = x
        
def birthdayMatch(people):
    """ 
    Find a peir of people with the same birthday in a room.
    Input: (name, birthday)
    Output: tuple of people names or None
    
    Complexity: O(n^2) 
        
    """
    n = len(people)                                 # O(1)
    # initialize static array record
    record = StaticArray(n)                         # O(n)
    
    for k in range(n):                              # n
        (name1, birthday1) = people[k]              # O(1)
        
        # check if in record
        for i in range(k):                          # k
            (name2, birthday2) = record.get_at(i)   # O(1)
            if birthday1 == birthday2:              # O(1)
                return (name1, name2)               # O(1)
        record.set_at(k, (name1, birthday1))        # O(1)
    return None 


