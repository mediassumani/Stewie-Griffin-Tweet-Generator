#!python
# The node class
class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# The doubly linked list class
class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def __str__(self):
        """Return a formatted string representation of this doubly linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'DoublyLinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""

        items = []
        current_node = self.head
        while current_node is not None:
            self.counter += 1
            items.append(current_node.data)
            current_node = current_node.next

        return items

    # Getter methods
    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    # function that retruns a boolean value if the list is empty or not
    def isEmpty(self):
        return self.head is None

    def length(self):
        counter = 0
        for item in self.items():
            counter += 1
        return counter

    def length_with_counter(self):
        return self.counter

    # This functions retruns a boolean on wheter or not the data is found in the list
    def find(self, quality):

        current_node = self.head
        while current_node is not None:
            if quality(current_node.data) is True:
                return current_node.data
            current_node = current_node.next

    # This function replaces a data from the list with a new one
    def replace(self, old_item, new_item):
        pass


    # This function adds the data given at the end of the list
    def insertTail(self, data):
        new_node = Node(data)
        new_node.next = None
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.counter += 1

    # This function deletes(more like detaches) the data at the end of list
    def deleteTail(self):
        if self.isEmpty() == True:
            print "The List is Empty"
        else:
            temp_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.counter -= 1
            return temp

        # This function adds the data given at the beginning of the list
    def insertHead(self, data):
        new_node = Node(data)
        if self.isEmpty() == True:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.counter += 1

    #This function deletes the head Node from the list
    def deleteHead(self):
        temp_node = self.head
        self.head = self.head.next
        self.head.prev = None
        if self.head == None:
            self.tail = None
            print "The List is Empty"
        self.counter -= 1
        return temp_node

    #This function deletes a Node from the list given a data
    def delete(self, data):
        if self.isEmpty() == True:
            print "The List is Empty"
            return
        else:
            current_node = self.head
            while(current_node.data is not data):
                current_node = current_node.next
            if current_node == self.head:
                self.deleteHead()
            elif current_node == tail:
                self.deleteTail()
            else:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

        print "The data is not found in the List"
