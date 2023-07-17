class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class Binary_Tree:
    def __init__(self):
        self.root = Node(None)

    def add(self, item):
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

    def dfs_inorder_recursive(self):
        if self.root is not None:
            self._dfs_inorder_recursive(self.root)

    def _dfs_inorder_recursive(self, node):
        if node.left is not None:
            self._dfs_inorder_recursive(node.left)
        print(node.value)
        if node.right is not None:
            self._dfs_inorder_recursive(node.right)

    def dfs_preorder_recursive(self):
        if self.root is not None:
            self._dfs_preorder_recursive(self.root)

    def _dfs_preorder_recursive(self, node):
        print(node.value)
        if node.left is not None:
            self._dfs_preorder_recursive(node.left)
        if node.right is not None:
            self._dfs_preorder_recursive(node.right)

    def dfs_postorder_recursive(self):
        if self.root is not None:
            self._dfs_postorder_recursive(self.root)

    def _dfs_postorder_recursive(self, node):
        if node.left is not None:
            self._dfs_postorder_recursive(node.left)
        if node.right is not None:
            self._dfs_postorder_recursive(node.right)
        print(node.value)


def main():
    """
            10
          /    \
        5       20
       / \     /  \
      2   8   14   30
    """
    t = Binary_Tree()
    t.add(10)
    t.add(5)
    t.add(20)
    t.add(2)
    t.add(8)
    t.add(14)
    t.add(30)

    print("Recursive Pre-order DFS:")
    t.dfs_preorder_recursive()

    print("Recursive In-order DFS:")
    t.dfs_inorder_recursive()

    print("Recursive Post-order DFS:")
    t.dfs_postorder_recursive()

if __name__=="__main__":
    main()

