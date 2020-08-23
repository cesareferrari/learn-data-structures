class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def remove_from_head(self):
        self.head = self.head.next
        self.length -= 1





# my_list = LinkedList()
# my_list.add_to_head(5)
# print('head', my_list.head.value)
# print('tail', my_list.tail.value)
# 
# my_list.add_to_head(8)
# print('head', my_list.head.value)
# print('next', my_list.head.next.value)
# print('tail', my_list.tail.value)
# 
# my_list.add_to_head(1)
# print('head', my_list.head.value)
# print('next', my_list.head.next.value)
# print('tail', my_list.tail.value)
