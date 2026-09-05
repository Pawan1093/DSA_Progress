n = 7789


reverse = 0

while n > 0:
    lastdigi = n % 10
   
    reverse = (reverse * 10) + lastdigi

    n = n // 10

print(reverse)



