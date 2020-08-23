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


node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4

linked_list = LinkedList(node1)


print(linked_list.index_of(15))
print(linked_list.index_of(25))

