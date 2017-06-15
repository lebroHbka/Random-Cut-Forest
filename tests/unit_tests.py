import unittest
from code.node import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.x1 = Node(0, 10, -2, 2, [(1, 2), (4, 1), (5, -2)])
        self.x2 = Node(-2, 2, -2, 2, [(-1, 0), (0, 0)])
        self.x3 = Node(-10, 10, 0, 21, [(-9, 10), (-7, 11), (-5, 0), (6, 21)])

    def test_get_longer_side(self):
        self.assertEqual(self.x1._get_longest_side(), 'x')
        self.assertEqual(self.x2._get_longest_side(), 'y')
        self.assertEqual(self.x3._get_longest_side(), 'y')

    def test_spliting(self):
        a, b = self.x1.make_2nodes_from_split()
        self.assertEqual(len(a.elements) + len(b.elements), len(self.x1.elements))
        a, b = self.x2.make_2nodes_from_split()
        self.assertEqual(len(a.elements) + len(b.elements), len(self.x2.elements))
        a, b = self.x3.make_2nodes_from_split()
        self.assertEqual(len(a.elements) + len(b.elements), len(self.x3.elements))



if __name__ == '__main__':
    unittest.main()