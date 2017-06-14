import anytree
from code.node import Node as MyNode

class Tree:
    def __init__(self, data_list, max_depth = 130):
        """
        datalist - [(x,y), (x,y), ...]
        """


        temp_root = MyNode(data_list)
        temp_root.sampling()

        self.root = anytree.Node(temp_root)
        self.max_depth = max_depth
        self._leafs_levels_list = []
        self.leafs_list = []
        self._tree(self.root, 1)
        # self.tree = [[node.name for node in children] for children in anytree.LevelOrderGroupIter(self.root)]

    def _tree(self, anytree_node, i):
        if i <= self.max_depth:
            if len(anytree_node.name.elements) > 1:
                left, right = anytree_node.name.spliting()
                a = anytree.Node(left, parent=anytree_node)
                b = anytree.Node(right, parent=anytree_node)
                self._tree(a, i + 1)
                self._tree(b, i + 1)
            elif len(anytree_node.name.elements) == 1:
                self._leafs_levels_list += [i]
                self.leafs_list += [anytree_node.name.elements[0]]

    @property
    def show(self):
        for pre, fill, node in anytree.RenderTree(self.root):
            print("%s%s" % (pre, node.name))

    @property
    def height(self):
        """
        :return: amount levels tree
        """
        return self.root.height + 1

    @property
    def leafs_count(self):
        """
        :return: amount of leafs

        """
        return len(self.root.name.elements)

    @property
    def leafs_level_position(self):
        return self._leafs_levels_list

    @property
    def leafs(self):
        return self.leafs_list

    # def __getitem__(self, item):
    #     return self.tree[item - 1]
