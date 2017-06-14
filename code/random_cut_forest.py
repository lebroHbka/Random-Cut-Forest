import anytree
import numpy as np
from code.tree import Tree

class RandomCutForest:
    def __init__(self, data_list, tree_count=100):
        data_list = [tuple([round(i[0], 7), round(i[1], 7)]) for i in data_list]
        self.data_len = len(data_list)

        self.data_dict = {i: {'total_leaf_lvl': 0, 'voted_tree_count': 0} for i in data_list}
        self.tree_forest = [Tree(data_list) for _ in range(tree_count)]

        for tree_in_forest in self.tree_forest:
            self.analyzer(tree_in_forest)
            # tree_in_forest.show

    def analyzer(self, tree):
        """

        anomal score = pow(2, -(   <middle node height> /
                                   (2 *(logn(<node counts>+0.5772156649)))
        """
        for number, node_tuple in enumerate(tree.leafs_list):
            # tick_value = np.log(tree.leafs_level_position[number])

            # self.data_dict[node_tuple]['total_leaf_lvl'] += tree.leafs_level_position[number]
            self.data_dict[node_tuple]['total_leaf_lvl'] += 1/tree.leafs_level_position[number]
            self.data_dict[node_tuple]['voted_tree_count'] += 1
        # for i in self.data_dict:
        #     if self.data_dict[i]['voted_tree_count']:
        #         print(i,self.data_dict[i], sep='=')
        # print('='*60)



    @property
    def get_result(self):

        result = []
        for node in self.data_dict:
            if self.data_dict[node]['voted_tree_count']:
                n = self.data_len
                a = (self.data_dict[node]['total_leaf_lvl'] / self.data_dict[node]['voted_tree_count'])
                b = (np.log(n - 1)) - (2*(n-1)/n)
                cof = a / b
                anomaly_score = a
                result += [[node[0], anomaly_score]]

        result.sort(key=lambda x:x[0])
        return result