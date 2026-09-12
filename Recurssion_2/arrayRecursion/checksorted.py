def sorted(arr, i):
    if i == len(arr) - 1:
        return True


    if arr[i] > arr[i+1]:
        return False


    return sorted(arr, i+1)


array = [12, 13, 11, 15, 17]
sorted(array, 0)