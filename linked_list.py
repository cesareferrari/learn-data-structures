# from the book "A common sense guide to data structures and algorythms"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def read(self, index):
        cur_node = self.head
        cur_idx = 0

        while cur_idx < index:
            cur_node = cur_node.next
            cur_idx += 1
            if not cur_node:
                return None

        return cur_node.data

    def index_of(self, value):
        cur_node = self.head
        cur_idx = 0

        while cur_node:
            if cur_node.data == value:
                return cur_idx

            cur_node = cur_node.next
            cur_idx += 1

        return None

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
            return

        cur_node = self.head
        cur_idx = 0

        # access the node before where the new node will go
        while cur_idx < index - 1:
            cur_node = cur_node.next
            cur_idx += 1

        # link new node to next
        new_node.next = cur_node.next
        cur_node.next = new_node


    def delete_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return

        cur_node = self.head
        cur_idx = 0

        while cur_idx < index - 1:
            cur_node = cur_node.next
            cur_idx += 1

        cur_node.next = cur_node.next.next



node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4

linked_list = LinkedList(node1)


print(linked_list.read(0))
print(linked_list.read(1))
print(linked_list.read(2))
print(linked_list.read(3))

linked_list.insert_at_index(2, 12)

print(linked_list.read(0))
print(linked_list.read(1))
print(linked_list.read(2))
print(linked_list.read(3))
print(linked_list.read(4))

linked_list.delete_at_index(3)

print(linked_list.read(0))
print(linked_list.read(1))
print(linked_list.read(2))
print(linked_list.read(3))
