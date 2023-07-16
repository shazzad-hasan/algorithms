import pptree

class Node:
    def __init__(self, name = None, children = None):
        self.name = name
        if children is None:
          children = []
        self.children = children
        self.parent = None

    def __str__(self):
        return self.name

    def add_child(self, node):
        node.parent = self
        assert isinstance(node, Node)
        self.children.append(node)

    def display(self):
      pptree.print_tree(self,'children','name', horizontal=False)

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
    r1 = Node("weather")
    t1 = Tree()
    t1.insert(r1, None)

    t1.insert(Node("sunny"), t1.nodes[0])
    t1.insert(Node("cloudy"), t1.nodes[0])
    t1.insert(Node("rainy"), t1.nodes[0])
    t1.insert(Node("humidity"), t1.nodes[1])
    t1.insert(Node("wind"), t1.nodes[3])
    t1.insert(Node("high"), t1.nodes[4])
    t1.insert(Node("normal"), t1.nodes[4])
    t1.insert(Node("strong"), t1.nodes[5])
    t1.insert(Node("weak"), t1.nodes[5])

    t1.root.display()

    print("\n")

    t2 = Tree()
    t2.insert(Node("shame"), None)

    t2.insert(Node("conscience"), t2.nodes[0])
    t2.insert(Node("selfdisgust"), t2.nodes[0])
    t2.insert(Node("embarrassment"), t2.nodes[0])

    t2.insert(Node("selfconsciousness"), t2.nodes[3])
    t2.insert(Node("shamefacedness"), t2.nodes[3])
    t2.insert(Node("chagrin"), t2.nodes[3])
    t2.insert(Node("discomfiture"), t2.nodes[3])
    t2.insert(Node("abashment"), t2.nodes[3])
    t2.insert(Node("confusion"), t2.nodes[3])

    t2.root.display()

if __name__=="__main__":
  main()