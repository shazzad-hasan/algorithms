class Node:
    def __init__(self, name = None, children = None):
        self.name = name
        if children is None:
          children = []
        self.children = children
        self.parent = None

    def add_child(self, node):
        node.parent = self
        assert isinstance(node, Node)
        self.children.append(node)

    def __str__(self):
        return self.name
    
    def dfs_preorder(self):
        print(self.name)
        for child in self.children:
            child.dfs_preorder()

    def dfs_inorder(self):
        if self.children:
            self.children[0].dfs_inorder()
        print(self.name)
        for child in self.children[1:]:
            child.dfs_inorder()

    def dfs_postorder(self):
        for child in self.children:
            child.dfs_postorder()
        print(self.name)


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, node, parent):
        if parent is not None:
            parent.add_child(node)
        else:
            if self.root is None:
                self.root = node
        self.nodes.append(node)

def main():
    """
        A
      /  \
     B     C
         /   \
        D     E
      
    """
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    t1 = Tree()
    t1.insert(a, None)
    t1.insert(b, a)
    t1.insert(c, a)
    t1.insert(d, c)
    t1.insert(e, c)

    print("\nPre-order traversal: ")
    t1.root.dfs_preorder()

    print("\nIn-order traversal:")
    t1.root.dfs_inorder()

    print("\nPost-order traversal")
    t1.root.dfs_postorder()


if __name__=="__main__":
  main()

