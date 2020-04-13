# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

        # add length for assitance in resize...
        # self.length = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    # THIS PART IS STRETCH
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            print("collision motha lova! @ key: " +
                  self.storage[index].key + " value: " + self.storage[index].value)
            print(f" would currently replace with key: {key} value: {value}")
            if key != self.storage[index].key:
                old_head = self.storage[index]
                # if self.storage[index].next is None:
                self.storage[index] = LinkedPair(key, value)
                self.storage[index].next = old_head
                # print(
                #     f"old head key: {old_head.key}, old head value: {old_head.value}")
                # print(
                #     f"new head key: {self.storage[index].key}, new head value: {self.storage[index].value}")
                print(
                    f"head: ({self.storage[index].key}, {self.storage[index].value}) -> head.next: ({self.storage[index].next.key}, {self.storage[index].next.value})")
                return
        self.storage[index] = LinkedPair(key, value)
        # my code from example i found for some help
        # print("the index made from hash_mod():", index)
        # if self.storage[index] is not None:
        #     for kv in self.storage[index]:
        #         # if key is found, then update
        #         # its current value to new value
        #         if kv[0] == key:
        #             kv[1] = value
        #             break

        # self.storage[index] = []
        # self.storage[index].append([key, value])
        # print(
        #     f"added value:{value} to key:{key} and key hashed to index:{index}")
        # return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        self.storage[index] = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get index just like in insert
        index = self._hash_mod(key)
        # return self.storage[index].value
        current = self.storage[index]
        while current is not None:
            if current.key == key:
                # return self.storage[index].value
                return current.value
            else:
                current = current.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create new array with size *2
        # use temp variable to store old storage info before messing with capacity
        old_storage = self.storage
        self.capacity *= 2
        # make the array new with new capacity
        self.storage = [None] * self.capacity
        # move the value over
        for pair in old_storage:
            if pair is not None:
                # figure out proper new place for k/v
                # re-insert key/value
                # self.insert(pair.key, pair.value)
                current = pair
                # this is where we look through the LL created and
                while current != None:
                    self.insert(current.key, current.value)
                    current = current.next
            # return None


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print("inserted 3 items")
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    print(f"testing resizing...\n")
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
