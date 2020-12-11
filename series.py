def fibonacci(n):
    if n < 0:
        print("This won't work, please try again")
    elif n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n < 0:
        print("This won't work, please try again")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0, y=1):  
    for i in range(n):
        x, y = y, x + y
    return x
