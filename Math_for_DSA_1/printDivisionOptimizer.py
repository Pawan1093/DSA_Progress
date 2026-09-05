num = 36

for i in range(1, int(num** 0.5) + 1):

    if i % num == 0:
        print(i)

        if i != num //i:
            print(num // i)