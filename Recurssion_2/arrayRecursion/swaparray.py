def swap(arr, left, right):
    if (left >= right):
        return


    arr[left], arr[right] = arr[right], arr[left]
    return swap(arr, left + 1, right - 1)


arr = [9, 2, 5, 4, 7, 3]
print(swap(arr, 0, len(arr) - 1))
print(arr)