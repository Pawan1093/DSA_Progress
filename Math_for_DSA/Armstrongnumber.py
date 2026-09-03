# An Armstrong number is a number equal to the sum of its digits, where each digit is raised to the power of the total number of digits.

n= 135
original = n
digitcount = len(str(original))

sum = 0

while(n>0):

    lastdigit = n % 10

    sum = sum + lastdigit ** digitcount

    n = n // 10


if sum == original:
    print("it is armstrong number")

else :
    print("Not Armstrong")


