class Node(object):
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return str(self.value)


def lca(node1, node2):
    """
    Return a least common ancestor.

    Memory and time complexity: O(s), where s is the distance between the two
    nodes.
    """
    if not isinstance(node1, Node) or not isinstance(node2, Node):
        raise TypeError("Inputs should be a Node.")

    ancestors = set()
    while node1 or node2:
        if node1:
            if node1 in ancestors:
                return node1
            else:
                ancestors.add(node1)
                node1 = node1.parent
        if node2:
            if node2 in ancestors:
                return node2
            else:
                ancestors.add(node2)
                node2 = node2.parent
    raise Exception("Least common ancestor not found.")


def main():
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node3 = Node(3, node1)
    node4 = Node(4, node2)
    node5 = Node(5, node2)
    node6 = Node(6, node3)
    node7 = Node(7, node3)
    node8 = Node(8, node4)
    node9 = Node(9, node4)

    print(lca(node1, node1))  # 1
    print(lca(node7, node7))  # 7
    print(lca(node1, node2))  # 1
    print(lca(node8, node9))  # 4
    print(lca(node8, node6))  # 1
    print(lca(node5, node9))  # 2


if __name__ == '__main__':
    main()
