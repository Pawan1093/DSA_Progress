def sumof(arr, i):
    if i == len(arr)-1:
        return arr[i]


    return arr[i] * sumof(arr, i+1)


arr = [5, 10, 12, 3, 12, 12]
print(sumof(arr, 0))