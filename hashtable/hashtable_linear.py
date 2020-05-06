"""
Linear HashTable
"""


class LinearHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity if capacity >= 8 else 8
        self.items = 0

    def hashing(self, key):
        hash_number = 5381
        for letter in key:
            hash_number = (hash_number << 5) + hash_number + ord(letter)
        return hash_number

    def hash_index(self, key):
        return self.hashing(key) % self.capacity

    def find(self, key):
        for index in range(len(self.storage)):
            if self.storage[index] is not None:
                if self.storage[index][0] == key:
                    return index
        return None

    def find_next(self):
        for index in range(len(self.storage)):
            if self.storage[index] is None:
                return index

    def load_factor(self):
        return self.items / self.capacity

    def put(self, key, value):
        load = self.load_factor()
        if load > 0.7:
            self.resize(self.capacity * 2)
        index = self.hash_index(key)
        if self.storage[index] is None:
            self.storage[index] = (key, value)
        else:
            found_index = self.find(key)
            if found_index:
                self.storage[found_index] = (key, value)
            else:
                next_index = self.find_next()
                self.storage[next_index] = (key, value)

    def get(self, key):
        found_index = self.find(key)
        if found_index is not None:
            return self.storage[found_index][1]
        return None

    def delete(self, key):
        found_index = self.find(key)
        if found_index is not None:
            self.storage[found_index] = None
        else:
            print(f"{key} was not found")

    def resize(self, hash_table_size):
        cur_storage = self.storage
        self.capacity = hash_table_size
        self.storage = [None] * self.capacity
        for index in range(len(cur_storage)):
            # print(f'Resizing Current Storage: {cur_storage[index]}')
            if cur_storage[index] is not None:
                self.put(cur_storage[index][0], cur_storage[index][1])


if __name__ == "__main__":
    lht = LinearHashTable(8)
    lht.put('key-1', 'val-1')
    lht.put('key-2', 'val-2')
    lht.put('key-3', 'val-3')
    lht.put('key-4', 'val-4')
    lht.put('key-5', 'val-5')
    lht.put('key-6', 'val-6')
    lht.put('key-7', 'val-7')
    lht.put('key-8', 'val-8')
    lht.put('key-9', 'val-9')
    lht.put('key-10', 'val-10')
    lht.put('key-11', 'val-11')
    lht.put('key-12', 'val-12')
    lht.put('key-13', 'val-13')
    lht.put('key-14', 'val-14')
    lht.put('key-15', 'val-15')
    lht.put('key-16', 'val-16')
