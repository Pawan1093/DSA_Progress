def reverse(arr, i):
    if i == len(arr):
        return 

    reverse(arr,i+1)
    print(arr[i])


arr = [1, 2, 3, 4, 5]
reverse(arr,0)