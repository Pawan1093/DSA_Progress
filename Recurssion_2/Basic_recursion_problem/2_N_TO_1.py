# Print N to 1

def N_TO_1(num):
    if (1>num):
        return

    print(num)
    N_TO_1(num-1)


N_TO_1(5)