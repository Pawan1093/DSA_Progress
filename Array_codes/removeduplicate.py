# Remove duplicates from sorted array in place


def removeDuplicate(arr):

    i = 0

    for j in range(1, len(arr)):

        if arr[j] != arr[i]:

            i += 1

            arr[i] = arr[j]

    return i + 1 


arr = [1, 1, 2, 2, 3, 3, 4]

k = removeDuplicate(arr)

print(k)
print(arr[:k])


