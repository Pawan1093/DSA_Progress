arr = [5, 6, 8, 9, 1, 2, 4, 7]

n = len(arr)

for i in range(n-1):
    swapped = False
    for j in range(n-1-i):


        if arr[j]> arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped =True

    if not swapped:
        break

print(arr)

# BEST CASE O(N)
# AVERAGE/ WORST = O(N*2)