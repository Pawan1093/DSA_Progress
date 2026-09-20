def zeroend(arr):

    i = 0

    for j in range(len(arr)):

        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr


arr = [0, 2, 0, 3, 5, 6, 8]

print(zeroend(arr))
