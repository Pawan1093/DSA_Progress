def partition(arr, low, high):

    pivot = arr[low]


    i = low -1 
    j = high+1


    while True:

        while True:

            i += 1

            if arr[i] >= pivot:
                break

        while True:

            j -= 1

            if arr[j] <= pivot:
                break

        if i >= j:
            return j


        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):

     if low < high:
         p = partition(arr, low, high)


         quicksort(arr, low, p)
         quicksort(arr, low, p+1)