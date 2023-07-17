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
    """
                   Weather
                /     |     \
            Sunny   Cloudy   Rainy
             /                  \  
        Humidity                Wind
        /    \                 /    \
    High   Normal          Strong   Weak
    
    """
    # nodes = ["weather", "sunny", "cloudy", "rainy", "humidity", "wind",
    #           "high", "normal", "strong", "weak"]

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

    print("Tree structure:")
    t1.root.display()

    print("\nNodes in the tree are:")
    for node in t1.nodes:
        print(node)

    print("\nNode at index 1: ", t1.nodes[1])
    print("\nParent of node at index 1 :", t1.nodes[1].parent)
    print("\nChild of node at index 1: ", t1.nodes[1].children[0])

if __name__=="__main__":
  main()