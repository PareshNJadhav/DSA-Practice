""""""
"""
Stack is LIFO,  we will use array or list to implement it, but remember if we add element to last every time its
O(1) and same for removing element from last O(1)

If this to be done for first index, list need reindexing making it O(n) , same for adding element and removing 
element.


"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            """different than normal prepend here we are pointing down side, i.e instead of top.next = new_node
            we are doing new_node.next = top """
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        """different than normal prepend here we are poping down side"""
        self.top = self.top.next
        temp.next = None

        self.height -= 1
        return temp


if __name__ == '__main__':
    stack = Stack(3)
    # stack.printStack()
    """test push"""
    # stack.push(4)
    # stack.push(5)
    # stack.printStack()
    """test pop"""
    stack.pop()
    stack.printStack()

