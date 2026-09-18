# 1st approach
arr = [5, 2, 5, 8, 2, 5]

freq = {}

for x in arr:
    freq[x] = freq.get(x,0)+1

# 2nd approach 

for x in arr:
    if x in freq:
        freq[x] += 1

    else:
        freq[x] = 1