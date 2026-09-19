# important

# find the second the largest element in the array without sorting it 

arr = [1, 2, 5, 9, 7]

largest  = 0
second_largest = 0

for i in range(len(arr)):
    if arr[i] > largest:
        largest  = arr[i]

for i in range(len(arr)):
    if arr[i] != largest and arr[i] > second_largest:
        second_largest = arr[i]

print("largest :", largest)
print("second largest :", second_largest)

