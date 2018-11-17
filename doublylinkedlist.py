from doubly_linked_list import DoublyLinkedList, Node
import unittest

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.counter == 0

    # function to test the printLinkedList() method
    def test_print_list(self):
        list = DoublyLinkedList()
        list.printLinkedList()
        list.insertHead("Medi")
        list.insertHead("Yves")
        list.insertHead("Jonas")
        list.printLinkedList()


    # Function to test finding a data from the list
    def test_find(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        dll.insertHead("Yves")
        dll.insertHead("Jonas")
        assert dll.find("Medi") is False
        assert dll.find("Yves") is True



    # Testing insterHead and insertTail Methods
    def test_data_insertion(self):
        list = DoublyLinkedList()
        list.insertHead("Medi")
        list.insertHead("Yves")
        list.insertHead("Jonas")
        assert list.isEmpty() is False
        assert list.length() == 3
        assert list.find("Yves") is True
        assert list.find("Marc") is False


if __name__ == '__main__':
        unittest.main()
