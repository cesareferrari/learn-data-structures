import unittest
from linked_list import Node
from linked_list import LinkedList

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_create_empty_list(self):
        self.assertEqual(self.linked_list.head, None)
        self.assertEqual(self.linked_list.tail, None)

    def test_add_to_head(self):
        self.linked_list.add_to_head(5)
        self.assertEqual(self.linked_list.head.value, 5)
        self.assertEqual(self.linked_list.tail.value, 5)

        self.linked_list.add_to_head(8)
        self.assertEqual(self.linked_list.head.value, 8)
        self.assertEqual(self.linked_list.tail.value, 5)

        self.linked_list.add_to_head(1)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 5)

    def test_add_to_tail(self):
        self.linked_list.add_to_tail(10)
        self.assertEqual(self.linked_list.tail.value, 10)
        self.assertEqual(self.linked_list.head.value, 10)

        self.linked_list.add_to_tail(45)
        self.assertEqual(self.linked_list.tail.value, 45)
        self.assertEqual(self.linked_list.head.value, 10)

        self.linked_list.add_to_tail(70)
        self.assertEqual(self.linked_list.tail.value, 70)
        self.assertEqual(self.linked_list.head.value, 10)

    def test_length(self):
        self.assertEqual(self.linked_list.length, 0)
        self.linked_list.add_to_head(3)
        self.linked_list.add_to_head(4)
        self.linked_list.add_to_head(5)
        self.assertEqual(self.linked_list.length, 3)

    def test_remove_from_head(self):
        self.linked_list.add_to_head(3)
        self.linked_list.add_to_head(4)
        self.assertEqual(self.linked_list.head.value, 4)

        self.linked_list.remove_from_head()
        self.assertEqual(self.linked_list.head.value, 3)

        self.linked_list.remove_from_head()
        self.assertEqual(self.linked_list.head, None)


if __name__ == '__main__':
    unittest.main()

