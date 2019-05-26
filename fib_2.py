def fib_print(n):
    """Print a Fibonaci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

fib_print(2000)

print(fib_print)

f = fib_print

f(100)

fib_print(0)


def fib_return(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib_return(100))