# A palindrome number is a number that stays the same when its digits are reversed
n = 121
origin = n

reverse = 0


while(n>0):

    lastdigit = n%10

    reverse = reverse * 10 + lastdigit

    n = n // 10

if reverse == origin:
    print("palindrome")
else:
    print("not palindrome")

