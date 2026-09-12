def palin(str, left, right):

    if left >= right:
        return True

    if str[left] != str[right]:
        return False


    return palin(str, left+1, right-1)
    


stri = "madamq"
print(palin(stri, 0, len(stri) - 1))