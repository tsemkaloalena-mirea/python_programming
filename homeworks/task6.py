class Node:
    def __init__(self, branch="", value=-1, x_num=-1):
        self.branch = branch
        self.value = value
        self.x_num = x_num
        self.nodes = []

    def add_node(self, branch="", value=-1, x_num=-1):
        self.nodes.append(Node(branch, value, x_num))


def create_tree(root):
    root.x_num = 4
    root.add_node(branch="LEX", x_num=1)
    root.nodes[0].add_node(branch="XBASE", x_num=2)
    root.nodes[0].nodes[0].add_node(branch="LOGOS", x_num=0)
    root.nodes[0].nodes[0].nodes[0].add_node(branch="GENIE", value=0)
    root.nodes[0].nodes[0].nodes[0].add_node(branch="STON", value=1)
    root.nodes[0].nodes[0].add_node(branch="VHDL", value=2)
    root.nodes[0].nodes[0].add_node(branch="POD", value=3)
    root.nodes[0].add_node(branch="ASN.1", x_num=3)
    root.nodes[0].nodes[1].add_node(branch="OPA", x_num=0)
    root.nodes[0].nodes[1].nodes[0].add_node(branch="GENIE", value=4)
    root.nodes[0].nodes[1].nodes[0].add_node(branch="STON", value=5)
    root.nodes[0].nodes[1].add_node(branch="QML", value=6)
    root.nodes[0].nodes[1].add_node(branch="MQL5", value=7)
    root.add_node(branch="AWK", value=8)
    root.add_node(branch="FISH", x_num=3)
    root.nodes[2].add_node(branch="OPA", value=9)
    root.nodes[2].add_node(branch="QML", value=10)
    root.nodes[2].add_node(branch="MQL5", value=11)


def count_tree(node, x):
    if node.x_num != -1:
        for next_node in node.nodes:
            if next_node.branch == x[node.x_num]:
                return count_tree(next_node, x)
    else:
        return node.value


def main(x):
    root = Node()
    create_tree(root)
    return count_tree(root, x)
