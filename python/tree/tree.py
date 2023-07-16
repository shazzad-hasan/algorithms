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

    def display(self):
      pptree.print_tree(self,'children','name', horizontal=False)

    def __str__(self):
        return self.name


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
    # -----  Test 1 -------
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

    # nodes = ["weather", "sunny", "cloudy", "rainy", "humidity", "wind",
    #           "high", "normal", "strong", "weak"]

    t1.root.display()

    print("Nodes in the tree are:")
    for node in t1.nodes:
        print(node)

    print("Node at index 1: ", t1.nodes[1])
    print("Parent of node at index 1 :", t1.nodes[1].parent)
    print("Child of node at index 1: ", t1.nodes[1].children[0])


    # ----- Test 2 -------
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    t2 = Tree()
    t2.insert(a, None)
    t2.insert(b, a)
    t2.insert(c, a)
    t2.insert(d, c)
    t2.insert(e, c)

    t2.root.display()


if __name__=="__main__":
  main()