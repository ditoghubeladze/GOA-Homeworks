def is_divisible(n,x,y):
    if n / x and n / y == n // x or n // y:
        return True
    elif n or x or y == 0:
        return False
    else:
        return False