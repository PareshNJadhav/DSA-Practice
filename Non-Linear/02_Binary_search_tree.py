""""""

"""
Binary Search Tree:
 
the key difference is if number is greater than node it goes to left and if its less than the node it goes right
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        # new_node = Node(value)
        # self.root = new_node
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        """works for root =None without check as well"""
        #if self.root is None: return None
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


if __name__ == '__main__':
    bst = BinarySearchTree()
    print(bst.root)
    """test insert"""
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(4)
    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)
    print(bst.root.right.right.value)
    print(bst.contains(2))
    print(bst.contains(44))