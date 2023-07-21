class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Binary_Search_Tree: 
    def __init__(self):
        self.root = Node(None) 
        
    def add(self, item):
        """ Add a new node in the tree """
        if self.root.value is None:
            self.root.value = item
        else:
            self._add(self.root, item)
        
    def _add(self, node, item):
        if item <= node.value:
            if node.left is not None:
                self._add(node.left, item)
            else:
                node.left = Node(item)
        else:
            if node.right is not None:
                self._add(node.right, item)
            else:
                node.right = Node(item)
            
    def search(self, item):
        """ Searches a node in the tree """
        if self.root.value is None:
            print(f"Node with item {item} doesn't exist.")
            return False
        else:
            return self._search(self.root, item)
    
    def _search(self, node,  item): 
        if node.value == item:
            print(f"Node with item {item} exists.")
            return True 
        
        elif item <= node.value:
            if node.left is not None:
                return self._search(node.left, item)
            else:
                print(f"Node with item {item} doesn't exist.")
                return False
        else:
            if node.right is not None:
                return self._search(node.right, item)
            else:
                print(f"Node with item {item} doesn't exist.")
                return False
            
    def remove(self, item):
        """ Removes a node from the tree """
        if self.search(item) is False:
            print(f"Node with item {item} doesn't exist.")
            return
            
        if self.root.value == item:
            # 1. Node to remove is a leaf node
            if self.root.left is None and self.root.right is None:
                self.root = None
            # 2. Node to remove has only left subtree
            elif self.root.left is not None and self.root.right is None:
                self.root = self.root.left 
            # 3. Node to remove has only right subtree
            elif self.root.left is None and self.root.right is not None:
                self.root = self.root.right 
            # 4. Node to remove has a both a left subtree and a right subtree
            else:
                self.root.value = self._most_left_node_from_right_subtree(self.root.right).value
                self._remove_item(self.root, self.root.right, self.root.value)
                
        elif item < self.root.value:
            self._remove(self.root, self.root.left, item)
        else:
            self._remove(self.root, self.root.right, item) 
            
    def _remove(self, parent, node, item):
        if item == node.value:
            # 1. Node to remove is a leaf node
            if node.left is None and node.right is None:
                if parent.left == node: 
                    parent.left = None 
                else:
                    parent.right = None
            # 2. Node to remove has only left subtree
            elif node.left is not None and node.right is None: 
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.right
            # 3. Node to remove has only right subtree
            elif node.left is None and node.right is not None:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            # 4. Node to remove has a both a left subtree and a right subtree
            else:
                node.value = self._most_left_node_from_right_subtree(node.right).value
                self._remove_item(node, node.right, node.value)
        elif item < node.value:
            self._remove_item(node, node.left, item)
        else:
            self._remove_item(node, node.right, item)
    
    def _most_left_node_from_right_subtree(self, node):
        """ Returns the left-most node from the right node """
        if node.left is None:
            return node 
        else:
            return self._most_left_node_from_right_subtree(node.left)
        
    def _remove_item(self, parent, node, item):
        if node.value == item:
            if parent.left == node:
                parent.left = None 
            else:
                parent.right = None
                
        elif item < node.value:
            self._remove_item(node, node.left, item)
        else:
            self._remove_item(node, node.right, item)

    def empty(self):
        """ Emptyies the tree """
        self.root = Node(None)
        
    def is_empty(self):
        """ Checks if the tree is empty """
        return self.root.value is None 
        
    def get_max_value(self):
        """ Return the max value in the tree """
        if self.is_empty():
            print("Empty tree")
            return False 
        
        node = self.root 
        while node.right is not None:
            node = node.right 
        return node.value 

    def get_min_value(self):
        """ Return the min value in the tree """
        if self.is_empty():
            print("Empty tree")
            return False 
        
        node = self.root 
        while node.left is not None:
            node = node.left
        return node.value 
    
def main():
    t = Binary_Search_Tree()

    print(t.is_empty())
    t.add(10)
    t.add(5)
    print(t.is_empty()) 
    t.empty()
    print(t.is_empty())
    print(t.get_max_value())
    print(t.get_min_value())

    """
            10
          /    \
        5       20
       / \     /  \
      2   8   14   30
    """
    t = Binary_Search_Tree()
    t.add(10)
    t.add(5)
    t.add(20)
    t.add(2)
    t.add(8)
    t.add(14)
    t.add(30)

    t.search(5)
    t.search(13)
    t.search(20)
    t.search(8)

    print(t.get_max_value())
    print(t.get_min_value())

    t.remove(2)
    t.search(2)

    t.remove(20)
    t.search(20)

if __name__=="__main__":
    main()
            
