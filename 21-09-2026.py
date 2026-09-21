# Largest element
# Smallest element
# Second largest
# Second smallest
# Reverse array
# Check if array is sorted
# Linear search
# Count even/odd
# Sum of array
# Count positive/negative

# question 1
def largest_number(array):

    largest = array[0]

    for i in range(len(array)):

        if array[i] > largest:

            largest = array[i]

    return largest

# print(largest_number([10, 12, 43, 12, 32, 1]))


# Question 2 

def smallest_element(array):

    smallest = array[0]

    for i in range(len(array)):

        if array[i] < smallest:

            smallest = array[i]

    return smallest

# print(smallest_element([0, 12, 43, 12, 32, -1]))


# Question 3 -  Second largest


def second_largest(array):

    largest = float('-inf')
    secondLarge = float('-inf')


    for i in range(len(array)):

        if largest < array[i]:

            secondLarge = largest
            largest = array[i]

        elif secondLarge < array[i] and secondLarge != largest:

            secondLarge = array[i]

    return secondLarge

# print(second_largest([0, 12, 43, 12, 32, -1]))

# Question 4 : - Second smallest


def second_smallest(array):

    smallest = float('inf')
    secondSmallest = float('inf')


    for i in range(len(array)):

        if  array[i] < smallest:

            secondSmallest = smallest
            smallest = array[i]

        elif array[i] < secondSmallest  and secondSmallest != smallest:

            secondSmallest = array[i]

    return secondSmallest

# print(second_smallest([0, 12, 43, 12, 32, -1]))



# Question 5 : Reverse array


def revserseArray(array):

    n = len(array)
    i = 0
    j = n-1

    while i < j:

        array[i], array[j] = array[j], array[i]

        i+=1
        j-=1

    return array

# print(revserseArray([12, 32, 43, 54, 76, 18]))

# Question - 6 - # Check if array is sorted


def checkSorted(array):

    i = 0
    sorted = False
    for j in range(1, len(array)):

        if array[j] >= array[i]:

            sorted = True
            i+=1

        else:
            sorted = False
            break

    return sorted

# print(checkSorted([12, 32, 43, 54, 76, 85]))

# Question 7 - # Linear search


def linearSearch(array, n):
    ok = ""
    for i in range(len(array)):

        if array[i] == n:
            return "element found at :" , i


        
    return "Not Found"

    

# print(linearSearch([12, 32, 43, 54, 76, 85], 54))

# Count even/odd


def evenOdd(array):

    even = 0 
    odd = 0

    for i in range(len(array)):

        if array[i] % 2 == 0:
            even+=1

        else:
            odd+=1

    return even, odd

# print(evenOdd([12, 32, 43, 54, 76, 85]))


# Question 8 - # Sum of array


def sumOfArray(array):
    total_sum = 0
    i = 0
    j = len(array) - 1

    while i <= j:
        if i == j:
            total_sum += array[i]
            break # Or just let i += 1 handle the loop exit
        else:
            total_sum += array[i] + array[j]
        
        # Pointers must ALWAYS update every turn
        i += 1
        j -= 1
            
    return total_sum

# print(sumOfArray([1, 2, 4, 5, 7, 8])) # Outputs: 27


# Question - 10 - # Count positive/negative


def countPosiNiga(array):

    positive = 0
    negative = 0

    for i in range(len(array)):

        if array[i] > 0:
            positive+=1

        else:
            negative+=1

    return positive, negative

print(countPosiNiga([10, 13, 43, -1, -3, 12, -43, 90]))
