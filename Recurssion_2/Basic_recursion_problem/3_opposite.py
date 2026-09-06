def opposite( num):
    if(1 > num):
        return 

    opposite(num-1)
    print(num)

opposite(5)