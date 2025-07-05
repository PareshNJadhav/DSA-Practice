class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def printQueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


if __name__ == '__main__':
    queue = Queue(3)
    queue.dequeue()
    #queue.printQueue()
    """test enqueue"""
    # queue.enqueue(4)
    # queue.enqueue(5)
    # queue.printQueue()
    """test dequeue"""
    queue.enqueue(4)
    queue.enqueue(5)
    queue.printQueue()
    #queue.printQueue()
    queue.dequeue()
    queue.printQueue()

"""
big O:
adding to queue =O(1)
removing item from queue = O(1)
"""