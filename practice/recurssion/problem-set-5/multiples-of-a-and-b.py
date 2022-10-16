def multiples(a, b):
    if b==0:
        return 0

    if b%2==0:
        return multiples(a+a, b//2)
    else:
        return multiples(a+a, b//2)+a


print( multiples(10,5) )