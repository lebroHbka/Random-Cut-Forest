from random import uniform, choice

class Node:
    def __init__(self, elements):

        self.elements = elements        # [(x,y), (x,y),....]


        self.l_border = min(elements, key=lambda x: x[0])[0] - 0.0000001
        self.r_border = max(elements, key=lambda x: x[0])[0] + 0.0000001
        self.b_border = min(elements, key=lambda x: x[1])[1] - 0.0000001
        self.t_border = max(elements, key=lambda x: x[1])[1] + 0.0000001


    def spliting(self):
        x = choice([0,1])
        if x == 1:
        # if self._get_longest_side() == 'x':
            return self._splite_x()
        else:
            if (len(self.elements) >= 2) and (self.elements[0][1] == self.elements[1][1]):
                return self._splite_x()
            else:
                return self._splite_y()

    def _splite_x(self):
        left_elem = []
        right_elem = []
        while (len(left_elem) == 0) or (len(right_elem) == 0):
            # print('-')
            border = uniform(self.l_border, self.r_border)
            left_elem = []
            right_elem = []
            for elem in self.elements:
                if elem[0] <= border:
                    left_elem += [elem]
                else:
                    right_elem += [elem]
        return Node(left_elem), Node(right_elem)

    def _splite_y(self):
        bot_elem = []
        top_elem = []
        while (len(bot_elem) == 0) or (len(top_elem) == 0):
            # print('=', self.elements)
            border = uniform(self.b_border, self.t_border)
            bot_elem = []
            top_elem = []
            for elem in self.elements:
                if elem[1] <= border:
                    bot_elem += [elem]
                else:
                    top_elem += [elem]

        return Node(bot_elem), Node(top_elem)

    # def _get_longest_side(self):
    #     return 'x' if (abs(self.l_border) + abs(self.r_border)) > (abs(self.b_border) + abs(self.t_border)) else 'y'

    def sampling(self, sampling_ratio=0.8):
        """

        input_ints(list) - list of total input numbers
        sampling_ratio(int) - how many numbers enter in total sampling

        :return list with sampling element
        """
        from random import shuffle

        sampling_elem_count = round(len(self.elements) * sampling_ratio)
        input_ints = self.elements.copy()
        shuffle(input_ints)

        self.elements = sorted(input_ints[:sampling_elem_count], key=lambda x: x[0])
        self.l_border = min(self.elements, key=lambda x: x[0])[0] - 0.0000001
        self.r_border = max(self.elements, key=lambda x: x[0])[0] + 0.0000001
        self.b_border = min(self.elements, key=lambda x: x[1])[1] - 0.0000001
        self.t_border = min(self.elements, key=lambda x: x[1])[1] + 0.0000001


    def show_node(self):
        return self.elements

    def __str__(self):
        return '{}'.format(self.elements)


