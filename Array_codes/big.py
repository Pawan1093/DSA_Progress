def smallest(arr):

    smallest = arr[0]

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest

    


def sec_smallest(arr):

    smallest = float('inf')
    secondSmallest = float('inf')


    for i in range(len(arr)):

        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]

        elif arr[i] < secondSmallest and arr[i] != smallest:
            secondSmallest = arr[i]

        return secondSmallest


def min_max(arr):
    min  = arr[0]
    max = 0

    for i in range(len(arr)):

        if arr[i] < min:
            min = arr[i]


        if arr[i] > max:
            max = arr[i]

    return min, max

print(smallest([5, 3, 5, 5, 6, 7, 1]))
print(sec_smallest([5, 3, 5, 5, 6, 7, 1]))
print(min_max([5, 3, 5, 5, 6, 7, 1]))