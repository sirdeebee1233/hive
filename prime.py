def isPrimeII(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if(n % i == 0):
            return False
        i += 2
    return True
