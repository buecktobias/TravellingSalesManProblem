class Leaf:
    def __init__(self, node):
        self.__parent = None
        self.__node = node
        self.__leafs = []

    def set_parent(self, leaf):
        self.__parent = leaf

    def get_node(self):
        return self.__node

    def delete_node(self):
        self.__node = None

    def get_parent(self):
        return self.__parent

    def add_leaf(self, leaf):
        if leaf not in self.__leafs:
            self.__leafs.append(leaf)

    def pop_leaf(self):
        return self.__leafs.pop()

    def has_leaf(self):
        return len(self.__leafs) > 0
