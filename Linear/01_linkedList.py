"""Why LinkedList?"""
"""
What is linked list?
A linked list is a linear data structure where elements (called nodes) are stored in separate memory locations and connected by pointers.

Each node contains:
Data
A pointer (reference) to the next node

Type	                            Description
Singly Linked List	    Each node points to the next only.
Doubly Linked List	    Each node points to next and previous.
Circular Linked List	Last node points to the first node again.

"""
"""
why Linked List?

Need fast insertions/deletions (especially in the middle or beginning).
Don’t know the size of data in advance.
Want to avoid memory reallocation (like in arrays).

"""
"""What makes it different from arraylist and array?

Feature	                Linked List	                    Array	           ArrayList (Java)
Memory Layout	Non-contiguous (pointers)	        Contiguous	         Contiguous (like array)
Access Time	O(n)    (sequential access)	         O(1)(direct index)	        O(1) (via index)
Insert/Delete	O(1) (head/middle)	            O(n) (shift needed)     	O(n) (shift, resize)
Resize	           No (dynamic by nature)	        Fixed size          	Automatically resizes
Extra Memory	    Yes (for pointers)              	No              	Some (for capacity)


Use Case	                                      Recommended Structure
Constant-time insert/delete at head	                Linked List
Frequent random access (by index)	                Array / ArrayList
Memory-constrained, read-heavy	                    Array / ArrayList
Implementing stacks/queues	                        Linked List (custom)
Real-time systems (predictable time)	            Array (no GC overhead)

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        # extra
        self.length = 1

    def printList(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = temp

        if self.head == self.tail:
            self.tail = None
            self.head = None

        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1

        return temp.value

    def pop1(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = temp

        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            # new_node.next = self.head
            # self.head = new_node

        self.length += 1

    def pop_first(self):
        # if self.head is None:
        if self.length == 0:
            return None
        # elif self.head.next is None:
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None

        self.length -= 1
        return temp.value

    def pop_first1(self):
        # if self.head is None:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # if index < 0 or index > self.length - 1:
        #     return None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length - 1:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        # bad approach o(n)
        # temp = self.get(index)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



if __name__ == '__main__':
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.printList()
    # print(linked_list.pop())
    # print(linked_list.pop())
    # print(linked_list.pop())
    # linked_list.prepend(3)
    # linked_list.prepend(2)
    """test pop_first"""
    # print(linked_list.pop_first())
    # print(linked_list.pop_first())
    # print(linked_list.pop_first())
    # print(linked_list.pop_first())
    # linked_list.printList()
    """test get"""
    # print(linked_list.get(4))
    # print(linked_list.get(2))
    # print(linked_list.get(-1))
    # print(linked_list.set_value(2, 8))
    """test insert"""
    # linked_list.insert(2,8)
    # linked_list.printList()
    # linked_list.insert(0,7)
    # linked_list.printList()
    # linked_list.insert(5,9)
    # linked_list.printList()
    """test remove"""
    # linked_list.remove(2)
    # linked_list.printList()
    # linked_list.remove(0)
    # linked_list.printList()
    # linked_list.remove(3)
    # linked_list.printList()
    # linked_list.remove(1)
    # linked_list.printList()
    """test reverse linked list"""
    linked_list.reverse()
    linked_list.printList()
    for i in range(3):
        print(i)