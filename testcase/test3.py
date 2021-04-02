import pytest

""" Worst case time complexity: O(n^2).
    Best case time complexity: O(1)
    Space complexity: O(n)
"""

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    if node1.value == node2.value:
        print(node1.value)
        return

    node1_array = [node1.value]
    node2_array = [node2.value]

    while True:
        if node1.parent:
            node1 = node1.parent
            if node1.value in node2_array:
                print(node1.value)
                return
            node1_array.append(node1.value)

        if node2.parent:
            node2 = node2.parent
            if node2.value in node1_array:
                print(node2.value)
                return
            node2_array.append(node2.value)

class Test3:

    n1 = Node(1, None)
    n2 = Node(2, n1)
    n3 = Node(4, n2)
    n4 = Node(7, n3)
    n5 = Node(8, n4)

    def test1(self, capsys):
        lca(self.n1, self.n1)
        out, err = capsys.readouterr()
        assert out == "1\n"
        assert err == ""

    def test2(self, capsys):
        lca(self.n5, self.n4)
        out, err = capsys.readouterr()
        assert out == "1\n"
        assert err == ""

    def test3(self, capsys):
        lca(self.n3, self.n2)
        out, err = capsys.readouterr()
        assert out == "2\n"
        assert err == ""

    def test4(self, capsys):
        lca(self.n5, self.n2)
        out, err = capsys.readouterr()
        assert out == "2\n"
        assert err == ""
