def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    """
    # TODO: implement Euclidean algorithm
    stop = 0
    gcd = 0

    while (stop == 0):
        c = a % b

        if c == 0:
            gcd = b
            stop = 1
        else:
            a = b
            b = c
    
    return gcd


print(gcd(61, 53))
