arr = [1, 3, 4 ,6, 8, 3, 9]

largest = 0

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)