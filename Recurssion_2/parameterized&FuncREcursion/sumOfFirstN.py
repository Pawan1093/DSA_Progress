# sum of first N number 

def summation(num , sum):
    if (num < 1):
        print(sum)
        return 


    summation(num-1, sum+num)


summation(10, 0)
