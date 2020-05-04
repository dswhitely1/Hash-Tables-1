class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash_number = 5381
        for letter in key:
            hash_number = (hash_number << 5) + hash_number + ord(letter)

        return hash_number

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            found_entry = None
            entry = self.storage[index]
            while entry.next is not None:
                if entry.key == key:
                    found_entry = entry
                entry = entry.next
            # Check if Entry is only one in hash table
            if found_entry is None and entry.key == key:
                found_entry = entry
            if found_entry is None:
                new_entry = HashTableEntry(key, value)
                entry.next = new_entry
            else:
                print(f'Found Value {found_entry.value}')
                found_entry.value = value
        else:
            entry = HashTableEntry(key, value)
            self.storage[index] = entry
        # entry = HashTableEntry(key, value)
        #
        #
        # if self.storage[index] is None:
        #     self.storage[index] = entry
        # else:
        #     found_entry = self.storage[index]
        #     while found_entry.next is not None:
        #         if found_entry.key == key:
        #             found_entry.value = value
        #         found_entry = found_entry.next
        #     found_entry.next = entry


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        value = None
        entry = self.storage[index]
        while entry.key != key and entry.next is not None:
            if entry.key == key:
                value = entry.value
            else:
                entry = entry.next
        # Check Last Entry
        if entry.key == key:
            value = entry.value
        return value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_3", "Successful ReWrite")
    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
