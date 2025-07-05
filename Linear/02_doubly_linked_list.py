
""" """
""" 
A Doubly Linked List is a type of linked list where:

Each node contains three parts:
Data
A pointer to the next node
A pointer to the previous node

 Why Use a Doubly Linked List?

Benefit	Explanation
🔁 Bidirectional traversal	- Easily move forward or backward in the list
🧹 Easier deletion	- You can delete a node without needing a previous pointer in advance
⚡ Efficient insertions/deletions - 	O(1) insert/remove if you have a reference to the node (especially in the middle)
🔄 Reversing is simple	- You can reverse the list with fewer operations compared to singly linked list

Use Cases for Doubly Linked List

Browser History	- You can go forward and backward between pages
Undo/Redo Functionality	- You can move both directions in a command history
Music/Video Playlist - Navigation	Skip to next/previous tracks easily
MRU/LRU Cache (e.g. in OS, DBs)	Fast removal of least-used items (often used in LinkedHashMap)
Deque (Double-Ended Queue)	- Inserting/removing from both ends is fast
Text Editors (Undo Stack)	- Track changes both ways
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if self.length < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
                # print("small")
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
                # print("large")
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if self.length < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if self.length < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        if temp:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp


if __name__ == '__main__':
    dll = DoublyLinkedList(4)
    """test append"""
    # dll.append(5)
    # dll.append(6)
    # dll.append(7)
    """test pop"""
    # dll.pop()
    # dll.printList()
    # dll.pop()
    # dll.pop()
    """test prepend"""
    # dll.pop()
    # dll.prepend(2)
    # dll.prepend(1)
    # dll.printList()
    """test pop_first"""
    # dll.append(5)
    # dll.append(6)
    # #dll.printList()
    #
    # dll.pop_first()
    # #dll.printList()
    # dll.pop_first()
    # #dll.printList()
    # dll.pop_first()
    # dll.printList()

    """test get"""
    # dll.append(5)
    # dll.append(6)
    # dll.append(7)
    # dll.append(8)
    # print(dll.get(1).value)
    # print(dll.get(3).value)
    """test set_value"""
    # dll.append(5)
    # dll.append(6)
    # dll.append(7)
    # dll.append(8)
    # dll.set_value(0,3)
    # dll.set_value(4,3)
    # dll.printList()
    """test set_value"""
    # (dll.pop())
    # dll.printList()
    # dll.insert(0, 1)
    # #
    # dll.insert(1, 3)
    # # dll.printList()
    # dll.insert(1, 2)
    # dll.printList()
    """test remove"""
    dll.append(5)
    dll.append(6)
    dll.remove(0)
    # dll.remove(0)
    # dll.remove(0)
    # dll.remove(0)

    dll.printList()
    dll.remove(2)
