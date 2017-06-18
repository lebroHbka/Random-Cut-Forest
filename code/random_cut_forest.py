import numpy as np
from code.tree import Tree


class RandomCutForest:
    def __init__(self, tree_count=100, sensitive=0.8, sampling_ratio=0.65, shingle=1, elements_count=500):
        """

        :param data_list:   <list>: list with data -> [(x1, y1), (x2, y2), ...] || (x1, y1)=tuple
        :param tree_count:  <int>: number of trees
        :param sensitive:   <int|float>: higher value -> lower sensitive(more penalty for node near root)
        :param shingle:     <int>: shingle -> dimensions numbers
        """
        self._tree_count = tree_count
        self._sensitive = sensitive
        self._sampling_ratio = sampling_ratio
        self._shingle = shingle
        self._elements_count = elements_count

    def fit(self, data_list):
        if self._elements_count == 0:
            self._data_dict = {i: {'total_leaf_lvl': 0, 'voted_tree_count': 0} for i in data_list}
            self._tree_forest = [Tree(data_list, self._sampling_ratio, self._shingle) for _ in range(self._tree_count)]
        elif len(data_list) < self._elements_count:
            raise Exception('Data set is lower than {}'.format(self._elements_count))
        else:
            self._data_dict = {i: {'total_leaf_lvl': 0, 'voted_tree_count': 0} for i in data_list[:self._elements_count]}
            self._tree_forest = [Tree(data_list[:self._elements_count], self._sampling_ratio, self._shingle) for _ in range(self._tree_count)]

    def update(self, new_point):
        pass


    def start(self):
        """
        ***Start alghoritm***
            Build forest
            Analise trees results

        :return: None
        """
        try:
            for tree_in_forest in self._tree_forest:
                # tree_in_forest.show()
                self._analyzer(tree_in_forest)
        except AttributeError:
            raise AttributeError('Try fit the model first!')

    def _analyzer(self, tree):
        for number, node_tuple in enumerate(tree.get_leafs_list()):
            leaf_lvl = tree.get_leaf_level_from_numb(number)
            self._data_dict[node_tuple]['total_leaf_lvl'] += 1 / np.power(leaf_lvl, self._sensitive)
            self._data_dict[node_tuple]['voted_tree_count'] += 1

    def get_result(self):
        result = []
        for node in self._data_dict:
            if self._data_dict[node]['voted_tree_count']:
                a = (self._data_dict[node]['total_leaf_lvl'] / self._data_dict[node]['voted_tree_count'])

                anomaly_score = a
                result.append([node[0], anomaly_score])

        result.sort(key=lambda x: x[0])
        return result
