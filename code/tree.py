import anytree
from code.node import Node as MyNode
from itertools import chain
import numpy.random as np_random


class Tree:
    def __init__(self, data_list, sampling_ratio, shingle,  max_depth=1000):
        """
        data_list - [(x,y), (x,y), ...]
        """
        self._elements_count = round(len(data_list) * sampling_ratio)
        self._shingle = shingle
        self._dimensional_count = 2 * shingle
        self._max_depth = max_depth
        # ---------------------------
        self._inputs_elements_count = self._elements_count          # for Vitter sampling

        # make start sampling and generate into n-dimensional
        elements_2ndim = self._make_start_sampling(data_list, data_list[:self._elements_count])
        self._elements, self._rest = self._generate_n_dimensional_elements(elements_2ndim)

        self._start()



    # ---------------- GETERS ----------------

    def get_element_count(self):
        return self._elements_count

    def get_inputs_elements_count(self):
        return self._inputs_elements_count

    def get_shingle(self):
        return self._shingle

    def get_leaf_level_from_numb(self, number):
        return self._leafs_level_list[number]

    def get_leafs_list(self):
        return self._leafs_list

    def get_leafs_level_list(self):
        return self._leafs_level_list

    def get_elements(self):
        return self._elements

    def get_dimensional_count(self):
        return self._dimensional_count

    def get_max_depth(self):
        return self._max_depth

    def get_root(self):
        return self._root

    def get_rest(self):
        return self._rest

    def get_rest(self):
        return self._rest



    # ---------------- SETERS ----------------

    def set_elements(self, value):
        self._elements = value

    def set_inputs_elements_count(self, value):
        self._inputs_elements_count = value

    def set_root(self, value):
        self._root = value

    def set_leafs_level_list(self, value):
        self._leafs_level_list = value.copy()

    def set_leafs_list(self, value):
        self._leafs_list = value.copy()

    def set_rest(self, value):
        self._rest = value



    def _start(self):
        # start building tree
        temp_root = MyNode(self.get_elements(), self.get_dimensional_count(), self.get_shingle())
        self.set_root(anytree.Node(temp_root))

        self._build_tree([self.get_root()], 1)
        leafs_list, leafs_level_list = self._make_leafs_lvl()

        self.set_leafs_level_list(leafs_level_list)
        self.set_leafs_list(leafs_list)

        # ------------------------------------------------

        # self.show()
        # p = (1, 10)
        # self._add_point(p)
        # self.show()
        # p = (2, 10)
        # self._add_point(p)
        # self.show()


    def _build_tree(self, anytree_node_list, i):
        if (i <= self.get_max_depth()) and len(anytree_node_list):
            splited_node_list = []
            for anytree_node in anytree_node_list:
                my_node = anytree_node.name
                if my_node.get_elements_count() > 1:
                    left, right = my_node.generate_2nodes_from_split()
                    l_node = anytree.Node(left, parent=anytree_node)
                    r_node = anytree.Node(right, parent=anytree_node)
                    splited_node_list.extend([l_node, r_node])
            self._build_tree(splited_node_list.copy(),  i+1)



    def _make_leafs_lvl(self):
        leafs_list = []
        leafs_lvl = []
        for node in anytree.LevelOrderIter(self.get_root()):
            if node.is_leaf:
                leafs_list.append(node.name.get_leaf()[:2])
                leafs_lvl.append(node.depth + 1)
        return leafs_list, leafs_lvl


    def update_tree(self, point):
        pass

    def _add_point(self, point):
        rest_and_raw_element = self.get_rest() + [point]

        # make n-dimensional new point
        point_insert_tree, rest = self._generate_n_dimensional_elements(rest_and_raw_element)
        point_insert_tree = point_insert_tree[0]
        self.set_rest(rest)

        print(point_insert_tree)

        # find were need insert new point -> merge with leaf
        leaf_to_merge_with_new_point = self._find_place_to_input(self.get_root(), point_insert_tree)


        if leaf_to_merge_with_new_point:
            # if new point is included in current bounding box

            # merge 2 leafs in 1 node
            node_merged_from2 = self._merge_2nodes(leaf_to_merge_with_new_point.name, [point_insert_tree])

            # make parent to <node_merged_from2>
            parent_of_leaf = leaf_to_merge_with_new_point.ancestors[-1]
            anytree_node_merged_from2 = anytree.Node(node_merged_from2, parent=parent_of_leaf)

            # add to all parent nodes new point
            for parent in leaf_to_merge_with_new_point.ancestors:
                parent.name.update_node_elements(point_insert_tree)

            # delete old leaf(he in merged_node)
            leaf_to_merge_with_new_point.parent = None

            # split new node for 2 leafs
            left, right = anytree_node_merged_from2.name.generate_2nodes_from_split()
            anytree.Node(left, parent=anytree_node_merged_from2)
            anytree.Node(right, parent=anytree_node_merged_from2)
        # else:


    def _merge_2nodes(self, node1, elements_from_node2):
        data = node1.get_elements()
        status = node1.get_status()
        data.extend(elements_from_node2)
        return MyNode(data, self.get_dimensional_count(), status=status)


    def _find_place_to_input(self, child, point):
        if child.is_root:
            root_borders = child.name.get_borders_decart()
            max_border, min_border = root_borders['max'], root_borders['min']
            if (point[0] > max_border[0]) or (point[1] > max_border[1]) or \
                                (point[0] < min_border[0]) or (point[1] < min_border[1]):
                return None

        if not child.is_leaf:
            mid_border = child.name.get_middle_border()
            if point[mid_border['dimension']] <= mid_border['value']:
                need_node = 'left'
            else:
                need_node = 'right'
            for child in child.children:
                if child.name.get_status() == need_node:
                    return self._find_place_to_input(child, point)
        else:
            return child


    def _del_point(self):
        pass

    # ---------------- SAMPLING ----------------

    def _make_start_sampling(self, full_data_list, start_list):
        for i in range(self.get_element_count(), len(full_data_list)):
            vitter = self._vitter_sampling()
            if vitter:
                start_list[vitter] = full_data_list[i]
        return start_list

    def _vitter_sampling(self):
        inputs_elements_count = self.get_inputs_elements_count()

        r = np_random.random_integers(0, inputs_elements_count)
        self.set_inputs_elements_count(inputs_elements_count + 1)
        if r < self.get_element_count():
            return r
        return None

    def _generate_n_dimensional_elements(self, element):
        result_to_return = []
        # last n*<shingle>-1 elements ignoring, cuz not enough elements to make n*<shingle>-dimensional
        # point
        last_element_number = len(element) - self.get_shingle() + 1

        for element_number in range(last_element_number):
            temp_ndim_elem = chain(*element[element_number:element_number + self.get_shingle()])
            result_to_return.append(tuple(temp_ndim_elem))
        return result_to_return, element[last_element_number:]






    # ---------------------- debuging ----------------------
    def show(self):
        for pre, fill, node in anytree.RenderTree(self._root):
            if node.is_leaf:
                print("%s|%s*****%s" % (pre, node.name, 0))
            else:
                print("%s|%s*****%s" % (pre, node.name, node.name.get_middle_border()))


