#!python

from linkedlist import LinkedList


# Thanks to vincenzo for this external method idea
def quality_check(key):
    """ Return a boolean value on wheter or not the key is found"""
    target_key = key

    def check_keys(node_data):
        """ Wrapper function that checks if the key passed matches"""
        node_key = node_data[0] # grabs the key from the tuple node
        return target_key == node_key

    return check_keys

def replace(old_item, new_item):
    pass


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for item in self.items():
            all_values.append(item[1])

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())

        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        counter = 0
        # iterates through the linked list of buckets
        for bucket in self.buckets:
            counter += bucket.length()

        return counter


    def _find_bucket(self, key):
        """ Returns the bucket linkedlist given the key"""
        # gets the index of the bucket from the array of buckets
        target_bucket_index = self._bucket_index(key)

        #returns the linkedList bucket that contains the key
        return self.buckets[target_bucket_index]

    def _find_node(self, key):
        """ Returns the node where the key belongs"""

        # gets the right bucket
        target_bucket = self._find_bucket(key)

        # trasversing the bucket linked list from the head
        current_node = target_bucket.head
        while current_node is not None:
            if current_node.data[0] == key:
                # returns the node if the firt element of its tuple is equal to the key
                return current_node
            current_node = current_node.next

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        target_item = self._find_node(key) # returns the node that contains the key
        return target_item is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""

        target_node = self._find_node(key)
        if target_node is not None:
            return target_node.data[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        target_bucket = self._find_bucket(key)
        target_node = self._find_node(key)

        # check if the node is empty, we update
        if target_node is None:
            # if there's nothing in the node, we add the new k,v pair
            self._find_bucket(key).append((key, value))
            return

        # if there is already a k,v pair, we overwrite it
        target_node.data = (key,value)


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        target_node = self._find_node(key)
        if target_node is None:
            # raise error if the node is empty
            raise KeyError('Key not found: {}'.format(key))
        # uses the ll's delete method to delete the node
        self._find_bucket(key).delete(target_node.data)


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
