import pptree

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

    def disp(self):
      pptree.print_tree(self,'children','name')

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
    r = Node("weather")
    t = Tree()
    t.insert(r, None)

    t.insert(Node("sunny"), t.nodes[0])
    t.insert(Node("cloudy"), t.nodes[0])
    t.insert(Node("rainy"), t.nodes[0])
    t.insert(Node("humidity"), t.nodes[1])
    t.insert(Node("wind"), t.nodes[3])
    t.insert(Node("high"), t.nodes[4])
    t.insert(Node("normal"), t.nodes[4])
    t.insert(Node("strong"), t.nodes[5])
    t.insert(Node("weak"), t.nodes[5])

    t.root.disp()

if __name__=="__main__":
  main()