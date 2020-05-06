class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_list(self, key, value):
        new_entry = HashTableEntry(key, value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_entry
            self.tail = new_entry
        else:
            new_entry.prev = self.tail
            self.tail.next = new_entry
            self.tail = new_entry

    def find_node(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()


class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def insert_after(self, key, value):
        current_next = self.next
        self.next = HashTableEntry(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = HashTableEntry(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity > 7 else 8
        self.storage = [None] * capacity
        self.items = 0

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
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def save(self, node_list, key, value):
        node_list.add_to_list(key, value)
        self.items += 1

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        load = self.items / self.capacity
        if load > .7:
            self.resize(self.capacity * 2)
        index = self.hash_index(key)
        if self.storage[index] is None:
            self.storage[index] = DoublyLinkedList()
        dll_list = self.storage[index]
        if dll_list.head is None:
            self.save(dll_list, key, value)
        else:
            found = dll_list.find_node(key)
            if found:
                found.value = value
            else:
                self.save(dll_list, key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index].find_node(key)
        if node:
            self.storage[index].delete(node)
            self.items -= 1
            load = self.items / self.capacity
            if load < .2:
                new_capacity = self.capacity // 2
                self.resize(new_capacity if new_capacity > 7 else 8)
        else:
            print(f'{key} was not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        found = None
        if self.storage[index] is not None:
            found = self.storage[index].find_node(key)
        if found:
            return found.value
        else:
            return None

        # value = None
        # entry = self.storage[index]
        # entry.find_node(key)
        # while entry is not None and entry.key != key and entry.next is not None:
        #     if entry.key == key:
        #         value = entry.value
        #     else:
        #         entry = entry.next
        # # Check Last Entry
        # if entry is not None and entry.key == key:
        #     value = entry.value
        # return value

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        old_storage = self.storage
        self.capacity = new_capacity
        self.items = 0
        self.storage = [None] * self.capacity
        for i in range(len(old_storage)):
            if old_storage[i] is not None:
                cur = old_storage[i].head
                while cur is not None:
                    key, value = cur.key, cur.value
                    self.put(key, value)
                    cur = cur.next



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
    print(ht.get("exist"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize(4)
    # new_capacity = len(ht.storage)
    #
    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    #
    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))
    #
    # print("")
