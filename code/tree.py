import anytree
from code.node import Node as MyNode


class Tree:
    def __init__(self, data_list, sampling_ratio, shingle,  max_depth=100000):
        """
        data_list - [(x,y), (x,y), ...]
        """

        temp_root = MyNode(data_list, sampling_ratio, shingle)
        temp_root.make_as_root_node()

        self._leafs_count = temp_root.get_elements_count()
        self._root = anytree.Node(temp_root)
        self._max_depth = max_depth
        self._leafs_level_list = []
        self._leafs_list = []
        self._build_tree(self._root, 1)

    def _build_tree(self, anytree_node, i):
        if i <= self._max_depth:
            my_node = anytree_node.name
            if my_node.get_elements_count() > 1:
                left, right = my_node.make_2nodes_from_split()
                l_node = anytree.Node(left, parent=anytree_node)
                r_node = anytree.Node(right, parent=anytree_node)
                self._build_tree(l_node, i + 1)
                self._build_tree(r_node, i + 1)
            elif my_node.get_elements_count() == 1:
                self._leafs_level_list.append(i)
                self._leafs_list.append(my_node.elements[0])

    def get_leaf_level_from_numb(self, number):
        return self._leafs_level_list[number]

    def get_leafs_list(self):
        """
        [(x1,y1), (x2, y2), ...] -> leafs list
        """
        return self._leafs_list

    # ---------------------- debuging ----------------------
    def show(self):
        for pre, fill, node in anytree.RenderTree(self._root):
            print("%s%s" % (pre, node.name))



    # @property
    # def get_height(self):
    #     """
    #     :return: max level of tree
    #     """
    #     return self._root.height + 1
    #
    # @property
    # def get_leafs_count(self):
    #     """
    #     :return: amount of leafs
    #
    #     """
    #     return self._leafs_count
    #
    #
    # def __getitem__(self, item):
    #     return self.tree[item - 1]

