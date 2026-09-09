def summation(num):
    if (num == 0):
        return 0

    return num + summation(num-1)

print(summation(3))