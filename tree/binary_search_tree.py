class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Binary_Tree: 
    def __init__(self):
        self.root = Node(None) 
    
    def empty(self):
        """ Emptyies the tree """
        self.root = Node(None)
        
    def is_empty(self):
        """ Checks if the tree is empty """
        return self.root.value is None 
        
    def add(self, item):
        """ Add a new node in the tree """
        if self.root.value is None:
            self.root.value = item
        else:
            self._add(self.root, item)
        
    def _add(self, node, item):
        if item < node.value:
            if node.left is not None:
                self._add(node.left, item)
            else:
                node.left = Node(item)
        elif item > node.value:
            if node.right is not None:
                self._add(node.right, item)
            else:
                node.right = Node(item)
        else:
            print(f"Node with item {item} already exists.")
            
    def search(self, item):
        """ Searches a node in the tree """
        if self.root.value is None:
            print(f"Node with item {item} doesn't exists.")
            return False
        else:
            return self._search(self.root, item)
    
    def _search(self, node,  item): 
        if node.value == item:
            print(f"Node with item {item} exist.")
            return True 
        elif item < node.value:
            if node.left is not None:
                return self._search(node.left, item)
            else:
                print(f"Node with item {item} doesn't exist.")
                return False
        elif item > node.value:
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
            
        if self.root.value is None:
            print(f"Node with item {item} doesn't exist.")
            return 
        if self.root.value == item:
            # no children
            if self.root.left is None and self.root.right is None:
                self.root = None
            # one left child
            elif self.root.left is None and self.root.right is not None:
                self.root = self.root.right 
            # one right child
            elif self.root.left is not None and self.root.right is None:
                self.root = self.root.left 
            # two children
            else:
                self.root.value = self._most_left_node_from_right_node(self.root.right).value
                self._remove_item(self.root, self.root.right, self.root.value)
                
        elif item < self.root.value:
            self._remove(self.root, self.root.left, item)
        else:
            self._remove(self.root, self.root.right, item) 
            
    def _remove(self, parent, node, item):
        if node is None:
            print(f"Node with item {item} doesn't exist.")
            return 
        if item == node.value:
            # no children
            if node.left is None and node.right is None:
                if parent.left == node: 
                    parent.left = None 
                else:
                    parent.right = None
            
            # one left child
            elif node.left is None and node.right is not None:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            
            # one right child
            elif node.left is not None and node.right is None: 
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.right
            
            # two children
            else:
                node.value = self._most_left_node_from_right_node(node.right).value
                self._remove_item(node, node.right, node.value)
    
    def _most_left_node_from_right_node(self, node):
        """ Returns the left-most node from the right node """
        if node.left is None:
            return node 
        else:
            return self._most_left_node_from_right_node(node.left)
        
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

    def inorder_traversal(self): 
        """ Return the inorder traversal of the tree """
        if self.root is not None:
            self._inorder_traversal(self.root)
    
    def _inorder_traversal(self, node): 
        if node.left is not None:
            self._inorder_traversal(node.left)
        print(node.value)
        if node.right is not None:
            self._inorder_traversal(node.right)
            
    def preorder_traversal(self):
        """ Return the pre-order traversal """
        if self.root is not None:
            self._preorder_traversal(self.root)
    
    def _preorder_traversal(self, node):
        print(node.value)
        if node.left is not None:
            self._preorder_traversal(node.left)
        if node.right is not None:
            self._preorder_traversal(node.right)
    
    def postorder_traversal(self):
        """ Return the post-order traversal """
        if self.root is not None:
            self._postorder_traversal(self.root)
    
    def _postorder_traversal(self, node):
        if node.left is not None:
            self._postorder_traversal(node.left)
        if node.right is not None:
            self._postorder_traversal(node.right) 
        print(node.value)
        
    def get_max_value(self):
        """ Return the max value in the tree """
        if self.root is None:
            print("Empty tree")
            return False 
        
        node = self.root 
        while node.right is not None:
            node = node.right 
        return node.value 

    def get_min_value(self):
        """ Return the min value in the tree """
        if self.root is None:
            print("Empty tree")
            return False 
        
        node = self.root 
        while node.left is not None:
            node = node.left
        return node.value 
            
            
# t = Binary_Tree()

# print(t.is_empty())
# t.add(10)
# t.add(5)
# print(t.is_empty()) 
# t.empty()
# print(t.is_empty())

# """
#         8
#        /  \
#       3   10
#      /  \    \
#     1   6    14
#        / \   /
#       4   7 13
#       \
#         5
# """
# t = Binary_Tree()
# t.add(8)
# t.add(3)
# t.add(6)
# t.add(1)
# t.add(10)
# t.add(14)
# t.add(13)
# t.add(4)
# t.add(7)
# t.add(5) 

# print("inorder traversal")
# t.inorder_traversal()

# print("preorder traversal")
# t.preorder_traversal()

# print("postorder traversal")
# t.postorder_traversal()

# t.search(6)
# t.search(13)
# t.search(100)
# t.search(8)

# print(t.get_max_value())
# print(t.get_min_value())

# t.remove(6)

# print("inorder traversal")
# t.inorder_traversal() 