import math
import random
from applications.hashtable.hash_table import HashTable

ht = HashTable(8)

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    key = str(x)+str(y)
    value = ht.get(key)
    if value is not None:
        return value
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        ht.put(key, v)
        return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
