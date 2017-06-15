from random import uniform, choice, shuffle


class Node:
    def __init__(self, elements, sampling_ratio, shingle):

        self.elements = elements                # [(x,y), (x,y),....]
        self._sampling_ratio = sampling_ratio
        self._shingle = shingle
        self._elements_count = len(elements)

        self.l_border = min(elements, key=lambda x: x[0])[0]
        self.r_border = max(elements, key=lambda x: x[0])[0]
        self.b_border = min(elements, key=lambda x: x[1])[1] - 0.0000001
        self.t_border = max(elements, key=lambda x: x[1])[1] + 0.0000001

        self.border = 0

    def make_as_root_node(self):
        self._sampling()

    def make_2nodes_from_split(self):
        x = choice([0,1])
        if x == 1:
            return self._splite_x()
        else:
            if (self.elements[0][1] == self.elements[1][1]):
                return self._splite_x()
            else:
                return self._splite_y()

    def _splite_x(self):
        left_elem = []
        right_elem = []
        fail_splits = []
        while (len(left_elem) == 0) or (len(right_elem) == 0):
            # print('-')
            border = uniform(self.l_border, self.r_border)
            if border in fail_splits:
                continue
            left_elem = []
            right_elem = []
            for elem in self.elements:
                if elem[0] <= border:
                    left_elem += [elem]
                else:
                    right_elem += [elem]
            fail_splits.append(border)
        return Node(left_elem, self._sampling_ratio, self._shingle), \
               Node(right_elem, self._sampling_ratio, self._shingle)

    def _splite_y(self):
        bot_elem = []
        top_elem = []
        fail_splits = []
        while (len(bot_elem) == 0) or (len(top_elem) == 0):
            # print('=', self.elements)
            border = uniform(self.b_border, self.t_border)
            if border in fail_splits:
                continue
            bot_elem = []
            top_elem = []
            for elem in self.elements:
                if elem[1] <= border:
                    bot_elem += [elem]
                else:
                    top_elem += [elem]
            fail_splits.append(border)
        return Node(bot_elem, self._sampling_ratio, self._shingle), \
               Node(top_elem, self._sampling_ratio, self._shingle)

    def _sampling(self):
        """
        *** IN PLACE ***
            Launching only 1 time, when creating root node
        """
        sampling_elem_count = round(len(self.elements) * self._sampling_ratio)
        self._elements_count = sampling_elem_count

        input_ints = self.elements.copy()
        shuffle(input_ints)

        self.elements = sorted(input_ints[:sampling_elem_count], key=lambda x: x[0])
        self.l_border = min(self.elements, key=lambda x: x[0])[0]
        self.r_border = max(self.elements, key=lambda x: x[0])[0]
        self.b_border = min(self.elements, key=lambda x: x[1])[1] - 0.0000001
        self.t_border = min(self.elements, key=lambda x: x[1])[1] + 0.0000001

    def get_elements_count(self):
        return self._elements_count

    # ---------------------- debuging ----------------------
    def show_node(self):
        return self.elements

    def __str__(self):
        return str(self.elements)




