import unittest

class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.l_child = left
        self.r_child = right

class Tree():
    def __init__(self, node_collection):
        self.level_count = {}
        self.level_sum = {}
        self.nodes = node_collection

    def heirarchy_level_avg(self, node, level=0):
        self.level_count[level] = 1 if self.level_count.get(level) is None else self.level_count.get(level)+1
        self.level_sum[level] = node.value if self.level_sum.get(level) is None else self.level_sum.get(level)+node.value
        if node.l_child is not None:
            self.heirarchy_level_avg(node.l_child, level+1)
        if node.r_child is not None:
            self.heirarchy_level_avg(node.r_child, level+1)

        if level != 0:
            return None

        level_avg = []
        for level in self.level_count:
            level_avg.append(self.level_sum[level]/self.level_count[level])

        return level_avg

class TestTree(unittest.TestCase):
    def test_tree1(self):

        n7 = Node(7)
        n15 = Node(15)
        n20 = Node(20, n7, n15)
        n9 = Node(9)
        n3 = Node(3, n9, n20)
        tree = Tree((n3, n9, n20, n15, n7))

        output = tree.heirarchy_level_avg(n3)
        self.assertEqual(output, [3, 14.5, 11])

unittest.main(exit=False)
