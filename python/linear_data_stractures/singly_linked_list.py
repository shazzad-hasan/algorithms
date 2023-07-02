class Node:
    def __init__(self, item):
        self.value = item
        self.next = None 

    def later_node(self, i):
        if i == 0:
            return self 
        assert self.next 
        return self.next.later_node(i-1)

    
class Singly_Linked_List:
    def __init__(self):
        self.head = None 
        self.size = 0

    def __len__(self):
        return self.size 

    def __iter__(self):
        node = self.head 
        while node is not None:
            yield node.value 
            node = node.next 
    
    def build(self, X):
        for x in reversed(X):
            self.insert_first(x)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.value 

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.value = x 

    def insert_first(self, x):
        temp_node = Node(x)
        temp_node.next = self.head 
        self.head = temp_node 
        self.size += 1 

    def remove_first(self):
        data = self.head.value 
        self.head = self.head.next 
        self.size -= 1 
        return data 

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return 
        new_node = Node(x) 
        pre_node = self.head.later_node(i-1)
        new_node.next = pre_node.next 
        pre_node.next = new_node 
        self.size += 1

    def remove_at(self, i):
        if i == 0:
            return self.remove_first()
        pre_node = self.head.later_node(i-1)
        data = pre_node.next.value 
        pre_node.next = pre_node.next.next 
        self.size -= 1
        return data 

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def remove_last(self):
        return self.remove_at(len(self)-1)

if __name__=="__main__":

    L = Singly_Linked_List()

    L.insert_first(31)
    L.insert_first(77)
    L.build([54, 24, 93, 17])

    for l in L:
        print(l) 

    print()
    print(len(L))
    print(L.get_at(1))
    L.set_at(1, 100)
    print(L.get_at(1))
    L.remove_first()
    print(L.get_at(0))
    L.remove_at(0)
    print(L.get_at(0))
    L.insert_last(15)
    print(L.get_at(len(L)-1))
    print(L.remove_last())
    print(L.get_at(len(L)-1))