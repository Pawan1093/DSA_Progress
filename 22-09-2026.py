"""DAY 2 — September 23
DSA

Arrays:

Move zeroes to end
Left rotate by one
Right rotate by one
Left rotate by D
Right rotate by D
Remove duplicates from sorted array

Then one unfamiliar Easy array problem"""

 # Question- 1 Move Zeros to end 


def moveZero(array):

    i = 0
    for j in range(len(array)):

        if array[j] != 0:

            array[i], array[j] = array[j], array[i]
            i += 1

    return array

# print(moveZero([0, 12, 13 , 0, 13, 134, 18, 0, 12]))

# Question2 : Left rotate by one

def leftrotate(array):

    for i in range(1, len(array)):
        array[i-1], array[i] = array[i], array[i-1]

    return array

# print(leftrotate([12, 32, 54, 87, 90]))
        

# Question 3 - Right rotate by one

def Rightrotate(array):

    for i in range(-1, 0):
        array[i], array[i+1] = array[i+1], array[i]

    return array

# print(Rightrotate([12, 32, 54, 87, 90]))

def rightrotate(array):

    temp = array[len(array)-1]

    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]

    array[0] = temp

    return array

# print(rightrotate([12, 32, 54, 12, 32, 91]))


# Question - Left rotate by D

def rotate(array, left, right):

    while left < right:

        array[left], array[right] = array[right], array[left]
        left+=1
        right-=1

    return array


array = [12, 13, 42, 87, 89, 97]
k = 3
ok = rotate(array,0, k-1)
ok = rotate(ok,k,len(ok)-1)
# print(rotate(ok,0, len(ok)-1))


# Question - 4 Right Rotation by d place 


def rotate1(array, left, right):

    while left < right:

        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    return array


array = [12, 32, 45, 54, 23, 98]
k = 2
n = len(array)

rotate1(array, 0, n-k-1)
rotate1(array, n-k, n-1)
rotate1(array, 0, n-1)

# print(array)

# question 5 - Remove duplicates from sorted array


def remove_duplicates(array):

    i = 0

    for j in range(1, len(array)):

        if array[j] != array[i]:

            i += 1
            array[i] = array[j]

    return i + 1


array = [1, 1, 2, 2, 3, 4, 4]

k = remove_duplicates(array)

print(k)
print(array[:k])


                  
     




















             