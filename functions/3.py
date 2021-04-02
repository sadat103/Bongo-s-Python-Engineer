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

