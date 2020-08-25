class Node:
    def __init__(self, value):
        self.value = value
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

        return cur_node.value

    def index_of(self, value):
        cur_node = self.head
        cur_idx = 0

        while cur_node:
            if cur_node.value == value:
                return cur_idx

            cur_node = cur_node.next
            cur_idx += 1

        return None

    def insert_at(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        cur_node = self.head
        cur_idx = 0

        while cur_idx < (index - 1):
            cur_node = cur_node.next
            cur_idx += 1

        new_node.next = cur_node.next
        cur_node.next = new_node
        


n0 = Node("banana")
n1 = Node("apple")
n2 = Node("fig")
n3 = Node("apricot")
n4 = Node("pear")

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

my_list = LinkedList(n0)

print(my_list.read(0))
print(my_list.read(1))
print(my_list.read(2))
print(my_list.read(3))
print(my_list.read(4))

my_list.insert_at(0, 'pineapple')

print(my_list.read(0))
print(my_list.read(1))
print(my_list.read(2))
print(my_list.read(3))
print(my_list.read(4))
print(my_list.read(5))
