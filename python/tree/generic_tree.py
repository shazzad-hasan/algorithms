class Node:
    def __init__(self, value):
        self.value = value 
        self.children = []
        self.parent = None 

    def add_node(self, node):
        node.parent = self
        assert isinstance(node, Node)
        self.children.append(node)


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, node, parent):
        if parent is not None:
            parent.add_node(node)
        if self.root is None:
            self.root = node 
        self.nodes.append(node)

if __name__=="__main__":
    r = Node(0)
    r.add_node(Node(1))
    r.add_node(Node(2))
    r.add_node(Node(3))

