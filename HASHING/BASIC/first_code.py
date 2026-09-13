# creating HASH TABLE 



arr = [2, 5, 2, 1, 5, 2, 3]

hash = [0] * 6

for X in arr:
    hash[X] += 1

print(hash)


# ----------------------------------------------

# arr = [4, 4, 2, 7, 2, 4]

# # Create hash table
# hash = [0] * 8

# # Store frequencies
# for x in arr:
#     hash[x] += 1

# # Queries
# print(hash[4])
# print(hash[2])
# print(hash[7])
# print(hash[6])


# Queries
# queries = [1, 3, 5, 4]

# for q in queries:
#     print(hash[q])