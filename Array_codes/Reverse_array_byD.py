# Question : Rotate the array By D place we are doing from both side if question asked from left side then function left and if by Right side then by right function 


def reverseByD(arr, left, right):

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]


        left += 1
        right -= 1


def leftrotate(arr, d):

    n = len(arr)

    d = d % n 

    reverseByD(arr, 0, d-1)

    reverseByD(arr, d, n-1)

    reverseByD(arr, 0, n-1)

    return arr


def rightrotate(arr, d):

    n = len(arr)

    d = d % n

    # Reverse first n-d elements
    reverseByD(arr, 0, n-d-1)

    # Reverse last d elements
    reverseByD(arr, n-d, n-1)

    # Reverse entire array
    reverseByD(arr, 0, n-1)

    return arr




arr = [1, 2, 3, 4, 5, 6, 7]
arr2 = [1, 2, 3, 4, 5, 6, 7]
d = 3

print(leftrotate(arr, d))

print(rightrotate(arr2, d))