class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    s_length = 1
    f_length = 2
    while fast.next is not None:
        print(f_length, s_length)
        if f_length - s_length == k:
            slow = slow.next
            s_length += 1
        fast = fast.next
        f_length += 1
    if f_length - s_length != k:
        return None
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 6
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
