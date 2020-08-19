"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev  # 1
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.length > 0:
            # 1. create node and insert before current head
            self.head.insert_before(value)
            # 2. update self.head
            self.head = self.head.prev

        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head

        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.length > 0:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        if self.length == 0:
            self.tail = ListNode(value)
            self.head = self.tail

        self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return
        elif self.tail == self.head:
            value = self.tail.value
            self.tail = None
            self.head = None
            self.length -= 1
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.length -= 1
            return value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node != self.head:
            # 1. remove
            # user dll delete function that calls the Node function
            self.delete(node)
            # 2. insert at head
            self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node != self.tail:
            self.delete(node)
            self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # empty list
        if not self.head and not self.tail:
            return
        # one item in the list
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node.prev is None: # node is the head
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
            
        node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        max = self.head.value
        cur_item = self.head

        while cur_item:
            if cur_item.value > max:
                max = cur_item.value

            cur_item = cur_item.next

        return max

