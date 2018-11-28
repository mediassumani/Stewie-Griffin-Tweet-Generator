#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.counter = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where  given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for item in self.items():
            all_keys.append(item[0])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Because we are looping through each bucket"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for item in self.items():
            all_values.append(item[1])

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Because we are looping through each bucket"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets: # O(n) time for looping through all buckets
            all_items.extend(bucket.items())

        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Because we are traversing ONLY eahh array element(buckets)"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        counter = 0
        # iterates through the linked list of buckets
        for bucket in self.buckets:
            counter += bucket.length()

        return counter

    def length_with_counter(self):
        """ Return the length of the key-value entries by keeping counter
        TODO: Running time: O(1) Because we are only returning a variable
        """
        return self.counter


    def _find_bucket(self, key):
        """ Returns the bucket linkedlist given the key
            TODO: Running time: O(n) beacuse we are only returning a variable
        """
        # gets the index of the bucket from the array of buckets
        target_bucket_index = self._bucket_index(key)

        #returns the linkedList bucket that contains the key
        return self.buckets[target_bucket_index]

    def _find_node(self, key):
        """ Returns the node where the key belongs
            TODO: Running time: O(n) beacuse we are trasversing each node
            Best case : O(1) if key is in head node and the linkedlist is empty
            Worst case : O(n) key is not in the bucket
        """

        # gets the right bucket
        target_bucket = self._find_bucket(key)
        # if target_bucket.head is not None:
        #     return

        # trasversing the bucket linked list from the head
        current_node = target_bucket.head
        while current_node is not None: # O(n) traversing each node
            if current_node.data[0] == key:
                # returns the node if the firt element of its tuple is equal to the key
                return current_node
            current_node = current_node.next

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(1) Because we are only returning a variable"""
        target_item = self._find_node(key) # returns the node that contains the key
        return target_item is not None # O(n) to return a boolean evaluation

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""

        target_node = self._find_node(key)
        if target_node is not None:
            return target_node.data[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(1) Because we are getting right into the correct node of the linkedList"""
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        target_bucket = self._find_bucket(key)
        target_node = self._find_node(key)

        # check if the node is empty, we update
        if target_node is None:
            # if there's nothing in the node, we add the new k,v pair
            self._find_bucket(key).append((key, value))
            self.counter += 1
            return

        # if there is already a k,v pair, we overwrite it
        target_node.data = (key,value)


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) Because we are getting right into the right of the linkedList"""
        target_node = self._find_node(key)
        if target_node is None:
            # raise error if the node is empty
            raise KeyError('Key not found: {}'.format(key))
        # uses the ll's delete method to delete the node
        self._find_bucket(key).delete(target_node.data)
        self.counter -= 1


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
