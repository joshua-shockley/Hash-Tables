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
        print("the index made from hash_mod():", index)
        if self.storage[index] is not None:
            for kv in self.storage[index]:
                # if key is found, then update
                # its current value to new value
                if kv[0] == key:
                    kv[1] = value
                    break

        self.storage[index] = []
        self.storage[index].append([key, value])
        # self.length += 1
        # print("length has changed upon insert:", self.length)
        print(
            f"added value:{value} to key:{key} and key hashed to index:{index}")
        return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        pass

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            for kv in self.storage[index]:
                if kv[0] == key:
                    return kv[1]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.


        Fill this in.
        '''
        # code from dynamic array.... what needs to be different to work for hashtable
        # need to also hash the key/value pairs
        # self.capacity *= 2
        # MAKES A NEW HASTABLE WHICH GRABS NEW MEMORY SLOT
        new_storage = HashTable(capacity=self.capacity*2)
        # NOW VERIFY THAT None IS THE VALUE IN STORAGE
        for i in self.storage:
            if self.storage[i] is None:
                continue

        # use key, value in self.storage.items()?
            for kv in self.storage[i]:
                new_storage.insert(kv[0], kv[1])
        self.storage = new_storage
        print("just changed capacity in fn resize() to:", self.capacity)
        return


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
