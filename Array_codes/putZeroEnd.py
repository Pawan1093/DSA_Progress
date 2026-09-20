def zeroend(arr):

    i = 0

    for j in range(1, len(arr)):

        if arr[i] == 0:

            arr[i], arr[j] = arr[j], arr[i]


        i+=1

    return arr

print(zeroend([0, 2, 0 , 3, 5, 6, 8]))
