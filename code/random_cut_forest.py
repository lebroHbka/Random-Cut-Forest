import numpy as np
from code.tree import Tree


class RandomCutForest:
    def __init__(self, data_list, tree_count=100, sensitive=0.8, sampling_ratio=0.55, shingle=1):
        """

        :param data_list:   <list>: list with data -> [(x1, y1), (x2, y2), ...] || (x1, y1)=tuple
        :param tree_count:  <int>: number of trees
        :param sensitive:   <int|float>: higher value -> lower sensitive(more penalty for node near root)
        :param shingle:     <int>: shingle -> dimensions numbers
        """
        self._data_dict = {i: {'total_leaf_lvl': 0, 'voted_tree_count': 0} for i in data_list}
        self._tree_forest = [Tree(data_list, sampling_ratio, shingle) for _ in range(tree_count)]
        self._sensitive = sensitive

    def start(self):
        """
        ***Start alghoritm***
            Build forest
            Analise trees results

        :return: None
        """
        for tree_in_forest in self._tree_forest:
            self._analyzer(tree_in_forest)
            # tree_in_forest.show()

    def _analyzer(self, tree):
        for number, node_tuple in enumerate(tree.get_leafs_list()):
            leaf_lvl = tree.get_leaf_level_from_numb(number)
            self._data_dict[node_tuple]['total_leaf_lvl'] += 1 / np.power(leaf_lvl, self._sensitive)
            self._data_dict[node_tuple]['voted_tree_count'] += 1

        # for i in self._data_dict:
        #     if self._data_dict[i]['voted_tree_count']:
        #         print(i, self._data_dict[i], sep='=')
        # print('='*60)

    def get_result(self):
        result = []
        for node in self._data_dict:
            if self._data_dict[node]['voted_tree_count']:
                a = (self._data_dict[node]['total_leaf_lvl'] / self._data_dict[node]['voted_tree_count'])
                anomaly_score = a
                result.append([node[0], anomaly_score])

        result.sort(key=lambda x: x[0])
        return result
