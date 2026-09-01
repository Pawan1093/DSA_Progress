n = 5


for i in range(1, n + 1):

    # spaces
    for j in range(n - i):
        print(" ", end="")

    # stars
    for j in range(2 * i - 1):
        print("*", end="")

    # next line
    print()


for i in range(1, n+1):

    for j in range(i):
        print(" ", end="")


    for j in range((2*n) - 2*i+1):
        print("*", end="")

    for j in range(i):
            print(" ", end="")

    print()



    