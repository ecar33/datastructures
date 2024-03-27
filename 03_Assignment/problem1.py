# Define hash functions and implementations for both methods

# Hash function 1 (common for both methods)
def hash1(x):
    return x % 10

# Second hash function for double hashing
def hash2(x):
    return 7 - (x % 7)

# Quadratic Probing insert function
def insert_quadratic_probing(hash_table, item):
    n = len(hash_table)
    index = hash1(item)
    i = 0
    while hash_table[(index + i**2) % n] is not None:
        i += 1
    hash_table[(index + i**2) % n] = item

# Double Hashing insert function
def insert_double_hashing(hash_table, item):
    n = len(hash_table)
    index1 = hash1(item)
    index2 = hash2(item)
    i = 0
    while hash_table[(index1 + i*index2) % n] is not None:
        i += 1
    hash_table[(index1 + i*index2) % n] = item

# Initialize hash tables
hash_table_quadratic = [None] * 10
hash_table_double = [None] * 10

# Insertions
insertions = [69, 48, 139, 648, 109, 75]

# Insert using Quadratic Probing
for item in insertions:
    insert_quadratic_probing(hash_table_quadratic, item)

# Insert using Double Hashing
for item in insertions:
    insert_double_hashing(hash_table_double, item)

print(f'{hash_table_quadratic}\n{hash_table_double}')
