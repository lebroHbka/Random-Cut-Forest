import numpy.random as np_random

# np_random.seed(1413151)

class Node:
    def __init__(self, elements, dimensional_count, status='None'):

        self._dimensional_count = dimensional_count
        self._status = status
        self._n_dimensional_elements = elements.copy()
        self._elements_count = len(elements)
        self._borders = self._generate_borders()


    # ---------------- GETERS ----------------
    def get_elements_count(self):
        return self._elements_count

    def get_elements(self):
        return self._n_dimensional_elements.copy()

    def _get_element(self, index):
        return self._n_dimensional_elements[index]

    def get_leaf(self):
        # return last avaliable element(calling on tree class, when elements_count is 1)
        return self._n_dimensional_elements[0]

    def get_borders_decart(self):
        """
            Not safe if changing answer
        """
        return {'min': self._borders['min'][:2], 'max': self._borders['max'][:2]}

    def get_status(self):
        return self._status

    def get_middle_border(self):
        return self._middle_border

    def get_dimensional_count(self):
        return self._dimensional_count



    # ---------------- SETERS ----------------

    def _set_middle_border(self, value):
        self._middle_border = value



    # ---------------- UPDATE ----------------

    def update_node_elements(self, new_element):
        self._n_dimensional_elements.append(new_element)



    # ---------------- SPLITS ----------------
    def generate_2nodes_from_split(self):
        dimension_to_cut = self._choice_random_dimension()

        i = 0
        j = 1
        while (self._get_element(i)[dimension_to_cut] == self._get_element(j)[dimension_to_cut]):
            if j < self.get_elements_count() - 1:
                j += 1
            else:
                i += 1
                if i >= self.get_elements_count() - 1:
                    dimension_to_cut = self._choice_random_dimension()
                    i = 0
                    j = 1
                else:
                    j = i + 1
        return self._splite(dimension_to_cut)

    def _choice_random_dimension(self):
        dimension_numbers = []
        # dimension_chances = []

        for i in range(self.get_dimensional_count()):
            dimension_numbers.append(i)
        # max_element = max(self.n_dimensional_elements, key=lambda x: x[i])[i]
        #     min_element = min(self.n_dimensional_elements, key=lambda x: x[i])[i]
        #     dimension_chances.append(max_element - min_element)
        #
        # total_value = sum(dimension_chances)
        # dimension_chances = list(map(lambda x: x/total_value, dimension_chances))
        # dimension_to_cut = np_random.choice(dimension_numbers, p=dimension_chances)
        dimension_to_cut = np_random.choice(dimension_numbers)
        return dimension_to_cut

    def _splite(self, dimension_to_cut):
        left_border = self._borders['min'][dimension_to_cut]
        right_border = self._borders['max'][dimension_to_cut]

        while True:
            border = self._generate_middle_border(left_border, right_border)

            left_elements, right_elements = list(), list()
            for n_dim_elem in self._n_dimensional_elements:
                if n_dim_elem[dimension_to_cut] <= border:
                    left_elements.append(n_dim_elem)
                else:
                    right_elements.append(n_dim_elem)
            if (len(left_elements) > 0) and (len(right_elements) > 0):
                break

        self._set_middle_border({'value': border, 'dimension': dimension_to_cut})

        n1, n2 = Node(left_elements, self._dimensional_count, status='left'), \
                 Node(right_elements, self._dimensional_count, status='right')

        return n1, n2



    # ---------------- BORDERS ----------------

    def _generate_borders(self):
        temp = {'min': [], 'max': []}
        for dimens_numb in range(self._dimensional_count):
            temp['min'].append(min(self._n_dimensional_elements,
                                            key=lambda x: x[dimens_numb])[dimens_numb])
            temp['max'].append(max(self._n_dimensional_elements,
                                            key=lambda x: x[dimens_numb])[dimens_numb])
        return temp

    def _generate_middle_border(self, left_border, right_border):
        return np_random.uniform(left_border, right_border)



    # ---------------- DEBUG ----------------
    def show_node(self):
        return self._n_dimensional_elements

    def __str__(self):
        return str(self._n_dimensional_elements)




